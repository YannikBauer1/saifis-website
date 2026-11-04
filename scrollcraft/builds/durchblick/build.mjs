// Publishes dist/: CSS inlined so nothing blocks the first paint, CSS and JS minified.
import { execSync } from 'node:child_process';
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const src = dirname(fileURLToPath(import.meta.url)), out = join(src, 'dist');
rmSync(out, { recursive: true, force: true }); mkdirSync(out);
const minCss = c => c.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\s+/g, ' ').replace(/ ?([{};,>]) ?/g, '$1').replace(/;}/g, '}').trim();
for (const f of ['assets']) cpSync(join(src, f), join(out, f), { recursive: true });
for (const f of ['favicon.ico', 'robots.txt', 'sitemap.xml', '_redirects']) if (existsSync(join(src, f))) cpSync(join(src, f), join(out, f));
for (const f of ['scrollcraft.js', 'durchblick.js', 'site.js']) {
  try { execSync(`npx -y esbuild@0.24.2 "${join(src, f)}" --minify --target=es2018 --outfile="${join(out, f)}" --log-level=error`, { stdio: 'pipe' }); }
  catch { cpSync(join(src, f), join(out, f)); }
}
for (const page of readdirSync(src).filter(f => f.endsWith('.html'))) {
  let h = readFileSync(join(src, page), 'utf8');
  h = h.replace(/<link rel="stylesheet" href="([\w.-]+\.css)">/g, (_, css) => `<style>${minCss(readFileSync(join(src, css), 'utf8'))}</style>`);
  h = h.replace(/<style>([\s\S]*?)<\/style>/g, (_, css) => `<style>${minCss(css)}</style>`);
  writeFileSync(join(out, page), h);
}
console.log('built', out);
