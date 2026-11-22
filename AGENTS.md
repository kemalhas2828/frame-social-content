# Instructions for an AI agent working in this repository

You are writing social media content for **Frame**, an independent café and bar at
7 Clifton Terrace, Finsbury Park, London N4 3JP (https://www.framefinsbury.co.uk).

## Do this
1. Read **`CONTENT-RULES.md`** in full before writing a single word. It is binding. It lists the
   facts you may state and the seven things you may never state.
2. Write **one post per file**, into `inbox/` only:
   `inbox/YYYY-MM-DD-<platform>-<slug>.md` — platform is `instagram`, `gbp` or `facebook`,
   and the date is the day the post should go out.
3. Copy the front matter from **`inbox/_TEMPLATE.md`**. Every field is required.
4. Worked example to match: `inbox/2026-11-25-instagram-matcha-morning.md`.

## Never do this
- Never edit, move or delete anything in `approved/` or `published/`.
- Never edit `README.md`, `CONTENT-RULES.md`, `AGENTS.md` or anything under `.github/`.
- Never invent a price, a dish, an opening hour, a dietary or allergen claim, an event, an
  offer, a capacity figure or an award. If you are not certain, write the uncertain part in
  square brackets — `[CONFIRM — …]` — and leave `status: draft`.
- Never shorten or substitute the four action URLs in `README.md`.

## If you cannot push
Open an issue instead, using the **Social post** issue template. That needs far less
permission than a commit, and the content will be filed from there.

A post in `inbox/` is a proposal, not a publication. Nothing here goes live automatically.
