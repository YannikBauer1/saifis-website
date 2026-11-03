# Objekt-Finder: brief

Authored decisions within the interview answers in `../../SHARED-BRIEF.md`. The owner chose this idea, "different per version" for audience, and "mix across versions" for boldness. Everything below marked authored was decided by the builder, not said by the owner.

## The eight topics

1. **Vibe (authored):** Saifi's own planning desk. Quiet, exact, useful. References: a craftsman's work order, a transit departure board, a well-kept building log.
2. **Scroll journey (authored):** the page is a tool. Object first, then footage and reasons, services, wish and place, next steps, who stands behind it, then a field to fill in.
3. **Energy curve (authored):** flat and calm. The only strong change is what the visitor triggers by picking an object.
4. **Feeling and memorable moment:** see below.
5. **The thing no other site does (authored):** the page reorganizes around your building and hands you a finished draft to send.
6. **Distance from premium-minimal (owner: mix across versions; authored for this one):** the calm, useful end of the mix. Dense, not minimal.
7. **One world or scenes (authored):** neither. A live surface.
8. **Assets (owner):** Instagram footage in `assets/instagram/`, current site colors, no paid generation.

Audience (authored): B2B decision-makers who know their building type and want a fast, specific answer.
Must believe: "Die haben so etwas schon gemacht und nehmen mir die Planung ab."
Action (owner): free analysis visit or direct call, both always in reach.

## Feeling curve

| Moment | Feeling | What causes it |
|---|---|---|
| Landing | Recognition | The surface is already set to a real job, with a Ford building moving in the frame |
| Picking an object | Being understood | Footage, reasons, service order and draft all change to match their building |
| Ticking services | Control | Each tick writes itself into the paper draft |
| Reading next steps | Calm | Three plain steps, free and without obligation |
| Who stands behind it | Trust | Real van, owner's name, the Q-Check |
| Filling in the field | Readiness | A cursor in a real input, the draft goes along |

## Peak

"Ich habe auf meine Objektart geklickt, und die ganze Seite hat sich auf mein Gebäude umgestellt."

It lives in the rail and panel at the top of the page. In a surface grammar the peak's scroll room is replaced by visible change: all fourteen services travel to new positions while the draft rewrites itself.

## Tell-someone sentence

It's the site where you click your kind of building, the whole page rearranges itself around it, and you end up with a finished cleaning plan draft to send off.

## Grammar: live surface

Why not the other seven: filmic, world and cutlist are about being carried, this visitor wants to operate something. Editorial is for reading. Poster has no use for footage. Gallery lacks the output. Split stage fits a two-sided argument, not nine object types.

Bans observed: no marketing bar, no full-bleed photography, no scrims, no scrub, no kinetic headlines, no display-size section headings. Largest heading is 1.625rem.

Honesty rule: every panel computes from data arrays in the page. No fake dashboard.

## Signature move: Der Reinigungsplan-Entwurf

One selection drives footage, proof label, reasoning, service order and suggestions, the items to clarify at the visit, and the draft. The draft composes the `mailto:` body, survives reload, and can be copied.

## Score, adapted to a surface

| Beat | Surface part | Behaviour |
|---|---|---|
| Recognition | Object rail with real thumbnails, status line | Already in a state on load |
| Being understood | Panel: clip, two stills, reasons | Swaps with no layout movement |
| Control | Service list, rhythm, place | Reorders by position only, ticks write into the draft |
| Calm | Next steps | Static |
| Trust | Van, owner, Q-Check | Static |
| Readiness | Inquiry form and phone | The page ends in an input |

Persistent throughout: rail, plan sheet (bottom sheet below 1180px), phone number.

## Engine

No engine JavaScript. A surface has no scroll choreography, so loading it would add nothing. Only `scrollcraft.css` is used, for tokens and browser surfaces. `html.sc-ready` and `data-sc-act="flow"` exist only so the harness can walk the page.

## Facts to confirm with Saifi

- Which services lead for each object, and all the "Klären wir beim Termin" items, are editorial suggestions.
- Plain-language service descriptions are written by the builder.
- All customer names and references need permission.
- Folder names are the only evidence that footage belongs to the named customer. Hescuro is confirmed by web search to be a rehab clinic group, so it sits under Gesundheit.
- GoFit is shown under the site's type "Sportclub", but it is a fitness studio.
- The Wohnanlage reference is one apartment, and the label says so.
