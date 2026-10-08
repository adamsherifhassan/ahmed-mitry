# Ahmed Mitry website

To preview it, double-click `index.html`.

## Adding new work (no code needed)
The website reads Ahmed's work straight from his Hygraph account every time someone visits.
To add a project:

1. Go to **app.hygraph.com**, sign in, and open the **Ahmed Mitry** project.
2. In the left sidebar, click **Content**, then **Project**.
3. Click **Add entry**.
4. Fill in the form:
   - **Title** (required). For example "Cairokee | New Song". A ` | ` or ` - ` between the artist and
     the title shows as a neat slash on the site.
   - **Type** (required). Pick **Music Production** or **Sound Design**. This decides which section
     the project appears in.
   - **Video url**. The YouTube, Instagram or podcast link. YouTube and Instagram links get a
     WATCH button. Kerning Cultures links get LISTEN.
   - **Thumbnail**. A landscape still from the video. On computers it floats next to the mouse when
     you hover the project. On phones it's the small picture beside the title.
   - **Client logo** (optional). Adds the logo to the Clients section.
5. Click **Save**, then **Publish**. Only published entries show on the site.
6. Refresh the website. The new project appears at the top of its section.

To change a project, open it, edit it, and click **Publish** again. To hide one, unpublish it.

If a project is published without a link it still shows, just without a WATCH button. Without a
thumbnail it shows a plain burgundy tile instead.

**Changing the opening photo.** It's the image on the first **Bio step** entry. Replace that
image and publish.

## What doesn't update on its own
- **Client names.** The line of names under the logos is fixed text in `index.html`.
- **Contact messages.** These are saved in Hygraph under Content → **message**, as on the
  previous site. There's no email alert, so check there for new enquiries.

## How it works
The page loads the latest **published** content from Hygraph on every visit, so there's no
rebuild and no code. It also ships with a saved copy of the content and images (in `img/`).
That copy is used if Hygraph can't be reached, so the site never shows up empty.

This only works once the site is online at a real web address. The private Claude preview link
shows a saved copy and doesn't update.

## Where it's hosted
Live at **https://adamsherifhassan.github.io/ahmed-mitry/**, hosted free on GitHub Pages from
Adam's repository `adamsherifhassan/ahmed-mitry`. Ahmed never needs to touch it, because new
work goes into Hygraph.

To change the design, edit `index.html` and push to the `main` branch. GitHub republishes it in
about a minute. A custom domain (for example ahmedmitry.com) can be added under the
repository's Settings → Pages.

## Design
See `DESIGN-SYSTEM.md` for the study of the Angus & Julia Stone site and how each part
maps onto this site.
