# Saifi's relaunch: shared brief for all four versions

Interviewed 2026-11-03. Everything below is shared. Each version has its own `builds/<name>/BRIEF.md`.

## What the owner of this project said

- "I don't like the three versions... The current website is obviously horrible."
- Color scheme "should be like the actual at the moment website".
- Use the Instagram images and videos in `assets/instagram/`.
- No paid image API. Missing images become prompts for ChatGPT or Codex.
- "multiple different versions, different ideas".
- Disliked in the old versions: "so many design faults", looked generic, no real footage, motion felt gimmicky.
- Customer per version: different per version. Boldness: mix across versions.
- Customer names and logos: show in prototypes, get permission before launch.
- End action: "book a free analysis visit or make a direct call. Like both of them are the important thing."
- Four complete pages in this first round.

## Verified facts (from the live site and Impressum, 2026-11-03)

- Saifi's Gebäudereinigung, Inhaber/Geschäftsführer Naqeeb Ullah Saifi
- Prinzregentenstraße 3, 97688 Bad Kissingen
- Telefon 0971 12382990 (`tel:+4997112382990`)
- info@saifis-gebaeudereinigung.de
- Instagram: saifis0077
- Van slogan, visible in footage: "Sauber. Schnell. Zuverlässig."
- Active "in Bad Kissingen und Umgebung"
- Services (14): Fassadenreinigung, Unterhaltsreinigung, Photovoltaikreinigung, Graffitientfernung, Treppenhausreinigung, Glasreinigung, Grundreinigung, Baureinigung, Hausmeisterservice, Polsterreinigung, Teppichreinigung, Steinreinigung, Jalousienreinigung, Desinfektionsreinigung
- Object types on the site: Bildungseinrichtung, Büro, Gesundheitseinrichtung, Handelsgeschäft, Kindergarten, Produktionsstätte, Sportclub, Wohnanlage
- Method on the site: Spezialisierung, individueller Reinigungsplan nach Analyse-Termin, Fachpersonal
- Persönlicher Ansprechpartner. Own "Q-Check System": unannounced regular quality checks of cleaning staff.
- Next steps on the site: Anfrage, kurzer Anruf und Termin, maßgeschneidertes Angebot
- Analyse-Termin is "kostenfrei" and "100% unverbindlich"
- Inhabergeführt; the owner personally vouches for satisfaction
- Legal pages exist: /impressum/ and /datenschutz/ on the current domain

The old hub's address "Kampfholz 95" and phone placeholder were wrong. Do not reuse them.

## Do not invent

No statistics, years in business, staff counts, response times, prices, certificates, Innung membership, review counts or star ratings, testimonials or quotes, insurance claims, or "Festpreis". No counters unless the number is real. If a claim is not listed above, leave it out.

## Actions

Two actions everywhere, one label each:
- `Analyse-Termin anfragen` (primary, opens the inquiry)
- `0971 12382990` as a real `tel:` link (equal importance, always reachable, sticky on phones)

There is no form backend. An inquiry must compose a real `mailto:` to info@saifis-gebaeudereinigung.de with the visitor's input in the body, and say honestly that it opens their mail app. Never show a false "sent" success. Never use a GET form that puts personal data in a URL.

## Brand

From the live site's computed styles and logo:
- `#006AB3` brand blue (link text, logo wordmark)
- `#0099FF` approx. bright logo blue (logo mark and "GEBÄUDEREINIGUNG")
- `#0F1D7B` deep navy (button text)
- `#BDD3E5` pale steel blue (button ground)
- `#EFF6FB` lightest blue tint
- `#FFFFFF`, and `#F8F8F8` page ground
- `#0C1115` near-black ink, `#6A6B6C` body grey (tint it toward blue)

Every version stays inside this blue and white family. Accent hue is always blue. Do not add green, orange or lime as design colors. Footage may contain them.

Logo: `scrollcraft/shared/logo.png` (500x250, transparent, small; request a vector for launch). The mark is two parallelograms forming an S with folded triangles. Do not redraw the wordmark. On dark grounds use the PNG inside a white area, or the white-mark treatment via CSS filter if it holds up visually.

## Media index (assets/instagram/, see sources.json)

Originals stay untouched. Encode copies into `builds/<name>/assets/`.

Strong stills:
- `Da7o21_DtGw-autohaus-loeffler/748552361_*` 1599x1248: silhouette of cleaner on ladder inside a dark window frame, bright sky behind. Luma-keyable.
- `Da7o21_DtGw-autohaus-loeffler/748986045_*` Ford tower glass building with logo, 752243110_* blue sky long facade, 748907717_* large sectional glass door, 748700694_* facade with sky.
- `DaVshbTjuxc-glasreinigung/730904856_*` cleaner on ladder under wood soffit, 1152x869 (face partly visible). 730919191_* tower facade 3024px. 730854673_* blue sky and building 3024px. 731769816_* HESCURO sign and sky 3024px. 732573208_* glass terrace 3024px.
- `Dd6sXijjpHi-lebenshilfe-hammelburg/828360922_*` Saifi's van side with logo and slogan, sharp, 1125x1500. 825270148_* and 827636745_* facades.
- `DUlheTnDor9-komplettreinigung-vorher-nachher/*` 13 stills 1152x1536 or 900x1200: apartment clear-out, trash piles, stained tiles, stained floor, under-sink. Find genuine matching before/after pairs by eye. Some may be the same state. Do not fake a pair: if no true after exists for a shot, say so and use it as a before only.

Strong clips (all silent as shipped; strip any audio):
- V20 `Dd6sXijjpHi-.../17962679049196826.mp4` 720x960 22.5s: water-fed pole against sun, water spray, Saifi's S shirt. Best footage. 11MB, needs trimming.
- V21 `Dd6sXijjpHi-.../17962679064196826.mp4` 720x960 9.3s: man in Saifi's shirt from behind, squeegee, blue sky.
- V19 `Dd6sXijjpHi-.../17962678656196826.mp4` 720x960 4.7s: facade tilt.
- V17 `DaVshbTjuxc-.../17949425550196826.mp4` 764x576 4.5s: man in safety harness washing glass above town.
- V15 `DaVshbTjuxc-.../17949425520196826.mp4` 764x576: inside glass hall, green outside. V16 `17949425541196826.mp4` 960x720 2.5s yellow apartment block. V18 `17949425616196826.mp4` 764x576 8.4s facade with red trim.
- V3 `DN1QZV3XCgD-gofit-fensterreinigung/760584610237917.mp4` 720x1280 39s: atrium glass, cleaner high on ladder, gym. Cut.
- V4 `DOt8tO0iGS9-autohaus-reel/1764003364239857.mp4` 720x1280 13.4s: dealership and van. V2 `DN1O_vF3Non-cupitalis-glasreinigung/1193007469330762.mp4` 480x854: van and building.
- V6, V7 `DUlekZxCHOj-solarreinigung/*` 360x480: brush on solar panels. Low resolution, keep small.
- V8, V9, V10 `DUlf9NQCEFW-hoch-und-glasreinigung/*` 480x640: V10 pole on Athera building. V9 worker face, indoor glass.
- V11, V12 `DUlheTnDor9-.../*` 480x640 60s: walk through the finished clean apartment. Cut.
- V13, V14 `Da7o21_DtGw-.../*` 592x464: Ford building glass, slow pan.
- V5 `DUleAt1CKXo-fitnessstudio/*` 480x854 and V1 `DI2BYoBsHDP-gofit-tuerreinigung/*` 848x480 4s: gym machines, GoFit doors.

Resolution law: nothing below 720px wide goes full-bleed on desktop. Low-res clips live in portrait frames at or near native size. The 3024px stills can bleed. Extract and inspect frames before committing to a shot. Some footage is shaky phone footage: pick the steady seconds.

## Customer names seen in footage

Autohaus Löffler (Ford), GoFit, Cupitalis, Lebenshilfe Hammelburg, Athera Physio, Hescuro. Shown in prototypes for impact. Record every use in your report so permission can be requested. Workers' faces also need consent.

## Design faults the owner will catch

The last round failed on this, so check it on the rendered page:
- Text overflow, clipped descenders, German long-word breaks. "Gebäudereinigung", "Photovoltaikreinigung", "Desinfektionsreinigung" are long: use `hyphens: manual` with `&shy;` where needed and test at 360px.
- Uneven card heights, orphan words, wrapped buttons, empty grid cells, misaligned baselines.
- Blank stages before a pinned act begins, dead scroll, cues that never reach full opacity.
- Low contrast over footage. Scrim only where text sits.
- Horizontal page scroll on phones. Sticky bars covering content or headings.
- Soft upscaled video, letterboxing, stretched images.
- Em dashes anywhere visible.

## Language and production

All visible copy in German, formal "Sie", specific and plain. Filler words and AI cadence are banned. `lang="de"`. Real SEO title and meta description naming the service and Bad Kissingen. LocalBusiness JSON-LD only with the verified facts above.

Google Fonts are acceptable in prototypes. Self-hosting is required before launch in Germany (flag in report).
