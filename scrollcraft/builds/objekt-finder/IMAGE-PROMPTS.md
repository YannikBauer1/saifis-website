# Image prompts for the Objekt-Finder

Three object types have no real footage: Büro, Kindergarten and Produktionsstätte. They currently show real shots from other jobs, honestly labelled "Beispielaufnahmen von anderen Objekten". The page is complete without these images. They are optional.

Paste each prompt into ChatGPT or Codex yourself. Nothing here calls a paid API.

**A generated image must never be presented as a real Saifi job.** Each one is captioned "Symbolbild". The real clip and the other still stay as they are, and the "Beispielaufnahmen" label stays.

## Output for every image

- Format: landscape 4:3, at least 1360x1020 px
- Save to `scrollcraft/builds/objekt-finder/assets/symbol/` under the name given below. Create the folder if needed.
- Convert to WebP if you can. PNG or JPG also works if you change the extension in the code.

## Shared style text

Use this unchanged at the start of every prompt, so the images look like one shoot:

> Realistic documentary photograph taken on a phone-quality but well-exposed camera, natural daylight, neutral white balance with slightly cool blue tones, ordinary German commercial building, clean and tidy but lived-in, no people visible, no text, no signs, no logos, no brand names, no watermarks, no readable labels. Straight verticals, eye-level camera, plain and unstaged, not glossy, not a stock-photo look, no illustration, no 3D render.

## 1. Büro

File: `assets/symbol/buero.webp`

> [shared style text] A corridor and open-plan office area in a mid-sized German company in a small town: grey carpet tiles, white walls, glass partition walls, plain desks, large windows with daylight and external blinds. Freshly cleaned, glass without streaks, nothing on the floor.

## 2. Kindergarten

File: `assets/symbol/kita.webp`

> [shared style text] An empty group room in a German kindergarten during the day: light linoleum floor, low wooden tables and small chairs, low shelves with neatly stored wooden toys, large low windows looking onto a garden with trees. No children, no drawings with writing, no name tags. Freshly cleaned floor.

## 3. Produktionsstätte

File: `assets/symbol/produktion.webp`

> [shared style text] Inside a small German production hall of a regional manufacturer during a pause: light grey coated concrete floor with yellow safety lines, plain machinery with no markings, steel columns, a large sectional door with glass panels and daylight coming through. No people. Swept and clean floor.

## Wiring one in

In `index.html`, find that object in the `OBJECTS` list and add `src` to its `a` entry, replacing `cap` and `alt`. Example for Büro:

```js
a: { src: 'assets/symbol/buero.webp', cap: 'Symbolbild: Büro', alt: 'Symbolbild eines aufgeräumten Büros mit Glaswänden und Fenstern' },
```

Use the same pattern for the others:

- Kindergarten: `src: 'assets/symbol/kita.webp'`, `cap: 'Symbolbild: Kindergarten'`
- Produktionsstätte: `src: 'assets/symbol/produktion.webp'`, `cap: 'Symbolbild: Produktionshalle'`

The rail thumbnail is separate. To change it, replace `assets/buero-t.webp`, `kita-t.webp` or `produktion-t.webp` with a 112x112 px crop.

Check each result before using it. Reject anything with readable text, logos, warped furniture, or a look too polished to sit next to the real footage.

## Better than any prompt

Real photos from Saifi would replace all of this. If there is a real office, kindergarten or production job, send 2 or 3 photos and a short clip, and the object can show "Referenz" instead.
