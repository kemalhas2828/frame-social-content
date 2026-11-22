# Frame Finsbury — social content drop

This repository is a **drop box for social media content**. An assistant (ChatGPT, or a
person) writes a post here as a Markdown file. Frame's growth agent reads this repository,
checks every post against the rules, and publishes the approved ones.

Nothing in this repository is published automatically. Writing a file here is a proposal.

---

## 1. Where a new post goes

One post = one file. Put it in `inbox/`, with this exact name:

```
inbox/YYYY-MM-DD-<platform>-<slug>.md
```

| Part | Allowed values |
|---|---|
| `YYYY-MM-DD` | the date the post is **intended to go out**, not today's date |
| `<platform>` | `instagram` · `gbp` · `facebook` |
| `<slug>` | short, lower case, hyphens only, e.g. `matcha-morning` |

Real example, already in this repository:

```
inbox/2026-11-25-instagram-matcha-morning.md
```

Never edit a file in `approved/` or `published/`. Those are the agent's.

---

## 2. What a post file looks like

Every file has YAML front matter and then the caption. Copy `inbox/_TEMPLATE.md`.

```markdown
---
platform: instagram          # instagram | gbp | facebook
format: feed-portrait        # feed-portrait | feed-square | story | reel | carousel | gbp-post
publish_date: 2026-11-25
action: MENU                 # ORDER | BOOK | MENU | ENQUIRE | NONE
action_url: https://www.framefinsbury.co.uk/pages/menu
image_brief: "what the photo or graphic should show — one sentence"
alt_text: "what is in the image, for a screen reader"
hashtags: [finsburypark, n4, londoncafe]
status: draft
---

The caption goes here. Plain text. Line breaks are kept.
```

### The four allowed actions
Every post carries exactly one. A post with no action is decoration.

| `action` | `action_url` |
|---|---|
| `ORDER` | `https://deliveroo.co.uk/menu/london/finsbury-park/frame-cafe-and-bar-7-clifton-terrace` |
| `BOOK` | `https://www.google.com/maps/reserve/v/dine/c/KCuCiXz5qt4` |
| `MENU` | `https://www.framefinsbury.co.uk/pages/menu` |
| `ENQUIRE` | `https://www.framefinsbury.co.uk/pages/private-hire` |

Do not invent a fifth destination and do not shorten these URLs.

---

## 3. Read this before writing anything

**`CONTENT-RULES.md` is binding.** It lists the facts you may state, and the things you must
never state. A post that breaks it is rejected, not corrected.

The short version: never invent a price, a dish, an opening hour, a dietary or allergen claim,
an event, a capacity figure, or an award.

---

## 4. Folders

| Folder | Meaning |
|---|---|
| `inbox/` | **write here.** Proposed posts, not checked yet |
| `approved/` | checked and cleared to publish — agent only |
| `published/` | live, with the date and link it went out on — agent only |
