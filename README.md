# Saifi's Gebäudereinigung – Website-Relaunch

Drei komplett neue One-Page-Entwürfe für https://saifis-gebaeudereinigung.de/ plus Analyse.
Jede Datei ist eigenständig (kein Build nötig): einfach im Browser öffnen.

| Datei | Richtung | Signature-Motion |
|---|---|---|
| `variante-a-frischluft.html` | hell, freundlich, lokal | Fensterwischer-Szene im Hero, schwebende Job-Karten, Zähler, Prozesslinie |
| `variante-b-nachtschicht.html` | dunkel, premium, plakativ | kinetische Headline, horizontal gepinnte Leistungskarten, Vorher/Nachher-Slider, Cursor-Spotlight |
| `variante-c-rhoen.html` | editorial, regional, konversionsstark | Formular im Hero mit Service-Chips, Kapitel-Navigation, Parallax-Bilder, gezeichnete Timeline |
| `saifis-relaunch.html` | Analyse-Hub (englisch) | Audit der aktuellen Seite, Wettbewerber, Vergleich der Varianten, To-do-Liste |

## Live-Vorschau (Claude Artifacts)

- Hub / Analyse: https://claude.ai/artifact/KqMQRkxnEsYGyQoY8BuvSe
- Variante A: https://claude.ai/artifact/Lc29kaZPc7mKYqkHPk4PE7
- Variante B: https://claude.ai/artifact/FrjhfPzN9ybTXX1AuBzWxC
- Variante C: https://claude.ai/artifact/Hdarwq4Z8ddQDBEZLufobe

## Technik

- Reines HTML/CSS/JS, GSAP 3.12 + ScrollTrigger via cdnjs, Google Fonts.
- Alle Animationen respektieren `prefers-reduced-motion`.
- Formulare zeigen nur einen Danke-Zustand; vor dem Livegang an einen Mailer (z. B. Formspree) anbinden.
- Platzhalter, die ersetzt werden müssen: Telefonnummer, E-Mail, Öffnungszeiten, Fotos, Impressum/Datenschutz-Links, Inhabername.

## Empfehlung

Struktur und Conversion-Logik aus Variante C übernehmen, optional das Hero-Motion aus A. Variante B ist die mutigste und würde als einzige dunkle Reinigungsseite der Region auffallen, braucht aber gute echte Fotos.
