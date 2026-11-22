"""Check every file in inbox/ before it is treated as a real proposal."""
import os, re, sys, datetime

PLATFORMS = {"instagram", "gbp", "facebook"}
FORMATS = {"feed-portrait", "feed-square", "story", "reel", "carousel", "gbp-post"}
ACTIONS = {
    "ORDER": "https://deliveroo.co.uk/menu/london/finsbury-park/frame-cafe-and-bar-7-clifton-terrace",
    "BOOK": "https://www.google.com/maps/reserve/v/dine/c/KCuCiXz5qt4",
    "MENU": "https://www.framefinsbury.co.uk/pages/menu",
    "ENQUIRE": "https://www.framefinsbury.co.uk/pages/private-hire",
    "NONE": "",
}
REQUIRED = ["platform", "format", "publish_date", "action", "action_url",
            "image_brief", "alt_text", "status"]
BANNED = [
    (r"£\s*\d", "a price - prices are never stated on social"),
    (r"\bloaded pancakes?\b", "a dish removed from the menu"),
    (r"\bpistachio french toast\b", "a dish removed from the menu"),
    (r"\bsalt beef\b", "a dish removed from the menu"),
    (r"\bgluten[- ]free\b", "a dietary claim - only the menu's own (GF) label may be carried"),
    (r"\bnut[- ]free\b", "a dietary claim that Frame does not make"),
    (r"\bhalal\b", "a dietary claim that Frame does not make"),
    (r"\bsuitable for coeliac", "a dietary claim that Frame does not make"),
    (r"\baward[- ]winning\b", "an unverifiable claim"),
    (r"\bbest (brunch|cafe|café|coffee) in\b", "an unverifiable superlative"),
    (r"\bvoted (number one|#1|best)\b", "an unverifiable claim"),
    (r"\b(deposit|minimum spend|late licence|late license)\b",
     "a private-hire term that may not be published"),
]
NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})-(instagram|gbp|facebook)-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

errors = []

def fail(f, msg):
    errors.append("%s: %s" % (f, msg))

inbox = "inbox"
if not os.path.isdir(inbox):
    print("no inbox/ directory"); sys.exit(1)

checked = 0
for name in sorted(os.listdir(inbox)):
    if not name.endswith(".md") or name == "_TEMPLATE.md":
        continue
    checked += 1
    path = os.path.join(inbox, name)
    m = NAME.match(name)
    if not m:
        fail(name, "filename must be YYYY-MM-DD-<instagram|gbp|facebook>-<slug>.md, "
                   "lower case, hyphens only")
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        fail(name, "missing YAML front matter"); continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(name, "front matter is not closed with ---"); continue
    fm_raw, body = parts[1], parts[2]
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    for key in REQUIRED:
        if not fm.get(key):
            fail(name, "front matter is missing '%s'" % key)
    if fm.get("platform") and fm["platform"] not in PLATFORMS:
        fail(name, "platform '%s' is not one of %s" % (fm["platform"], sorted(PLATFORMS)))
    if m and fm.get("platform") and fm["platform"] != m.group(2):
        fail(name, "platform '%s' does not match the filename" % fm["platform"])
    if fm.get("format") and fm["format"] not in FORMATS:
        fail(name, "format '%s' is not one of %s" % (fm["format"], sorted(FORMATS)))
    act = fm.get("action")
    if act and act not in ACTIONS:
        fail(name, "action '%s' is not one of %s" % (act, sorted(ACTIONS)))
    elif act and act != "NONE" and fm.get("action_url") != ACTIONS[act]:
        fail(name, "action_url for %s must be exactly %s" % (act, ACTIONS[act]))
    if fm.get("publish_date"):
        try:
            d = datetime.date.fromisoformat(fm["publish_date"])
            if m and m.group(1) != fm["publish_date"]:
                fail(name, "publish_date does not match the date in the filename")
        except ValueError:
            fail(name, "publish_date must be YYYY-MM-DD")
    words = len(body.split())
    if words < 15:
        fail(name, "caption is only %d words - too thin to publish" % words)
    if fm.get("platform") == "gbp" and len(body) > 1500:
        fail(name, "a Google Business Profile post must be under 1500 characters")
    low = body.lower()
    for pat, why in BANNED:
        hit = re.search(pat, low)
        if hit:
            fail(name, "caption contains %r - %s" % (hit.group(0), why))
    place = ("finsbury park", "n4", "stroud green")
    if not any(p in low for p in place):
        fail(name, "caption never names the neighbourhood (Finsbury Park, N4 or Stroud Green)")

print("checked %d post(s) in inbox/" % checked)
if errors:
    print("\nREJECTED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print("all posts pass")
