# Design system: Angus & Julia Stone → Ahmed Mitry

Studied from angusandjuliastone.com on 8 Oct 2026: its theme stylesheet
(`wp-content/themes/ajstone/style.css`), its page-specific styles, and the live page at
desktop (1440px) and phone (375px) widths.

## 1. Typography

| Role | AJS original | Ahmed Mitry site (free Google Fonts equivalent) |
|---|---|---|
| Everything: body, nav, buttons, list rows | **Highway 70 Cond** (condensed serif), 24px, line-height 1.4 | **Instrument Serif**, 24px (20px on phones) |
| Section headings (h2–h4) | **Aston Script Bold** (copperplate script), 40px; centred headings 80px (50px phone) | **Imperial Script**, 58–92px. Its looped capitals are the closest free match to Aston (chosen over Great Vibes in v2) |
| Logo | Hand-drawn brush signature (PNG, white over the photo, black once scrolled, gold in the footer) | **Mrs Saint Delafield** set as live text, so it can change colour the same way |
| Hero title | Gold embroidered lettering (image): "Karaoke" in serif, "Bar" in script | "Ahmed" in Instrument Serif and "Mitry" in **Great Vibes**, in stitched-thread gold (the original v1 style, restored at the user's request) |
| Small utility text | Inter (only inside the tour widget) | Inter, 11–15px, for form helper text only |

Other rules from the original:
- h1 100px (60px on phones)
- `em`/`i` are never italic; they switch to the serif face (used for small labels like "New Album")
- small print is 14–16px with line-height 1.8
- nav links are uppercase, 16px

## 2. Colour

| Token | Value | Use |
|---|---|---|
| paper | `#ffffff` | Page background (the whole site is white) |
| black | `#000000` | Body text, section rules |
| ink | `#2b292a` | Form text, borders, menu text |
| wine | `#612c34` | Buttons, row hover fill, footer background |
| gold | `#f5cd76` | Button text, footer text, hero lettering |
| veil | `rgba(0,0,0,.6)` | Overlay behind the open menu |

The site is light-only on purpose; there is no dark mode.

## 3. Components

**Pill button.** Wine fill, gold uppercase text, 1px wine border, radius 30px, padding `5px 50px 3px`, line-height 38px, 24px text (18px on phones). On hover it turns transparent with wine text. Every transition is `0.4s ease-in-out`.

**Outline pill.** The RSVP button's style: a thin wine outline with an icon. Here it's each project's WATCH (play icon) or LISTEN (sound bars) button. When the row fills wine on hover, it turns solid gold.

**Link underline.** A 2px bar under the link grows from 0 to full width on hover (1px in the footer).

**List row (tour dates → projects).** The list has a 1px top rule and each row has a 1px bottom rule. Columns are text on the left, location in the middle, buttons on the right. On hover a wine fill rises from the bottom (`height 0 → 100%`) and all text and borders turn gold. On phones the columns stack.

**Section divider.** A plain 1px black rule between blocks, with about 30px of padding.

**Centred block (Online Store / Be in the know → Clients).** Big centred script heading, then a single pill, between rules.

**Header.** Transparent over the hero, with a white logo and white uppercase nav. Once you scroll, it becomes fixed and 90% white with a soft `0 0 50px rgba(0,0,0,.1)` shadow, and the logo and nav turn dark. The logo shrinks from 100px to 70px tall.

**Menu (phones).** A three-line burger icon opens a white panel that slides in from the left (100% wide on phones, 50% on desktop) over a 60% black overlay. Links are uppercase, 20px. The close X rotates 90° on hover.

**Footer.** Wine background with all text gold. The logo is on the left and the social links (Instagram, Facebook, LinkedIn, as on the old site) are on the right, with the copyright underneath.

## 4. Layout and photography

- Container: 40px side padding (15–16px on phones). Max width steps 1024 → 1200 → 1400 → 1480px as the screen widens.
- The hero is a full-screen photo with the title and one button centred. There's a separate portrait crop for phones.
- Photos have a warm, grainy, analogue-film look. Here that's recreated with a CSS film-grain layer plus a light sepia and contrast treatment.
- There are few images overall and lots of white space. The only things that move are hover effects.
- Ahmed's site uses exactly one photograph, the hero. Project stills appear only as a floating preview when you hover a row on desktop, and as small thumbnails in the rows on phones.

## 5. Mapping of sections

| AJS | Ahmed Mitry |
|---|---|
| Hero "Karaoke Bar" + OUT NOW / BUY HERE | Hero "Ahmed Mitry" + WATCH THE WORK |
| Upcoming Shows (tour rows, RSVP / TICKETS) | Two sections, as on the old site's separate pages: **Music Production** (15) and **Sound Design** (12). Each has its own ruled list, WATCH / LISTEN, and "Show all" |
| (no equivalent) | Statement band: wine with gold type, replacing The Story |
| Online Store / Be in the know | Clients: logos and client names |
| Contact page (photo header + form) | Contact form only, with no photo (saves to Hygraph "Message", as before) |
| Wine footer | Wine footer |
