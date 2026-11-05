"""Bouwt de LocalBuddy-demo.

- local/LocalBuddy-offline.html  volledige demo zonder login (alleen lokaal, staat niet in git)
- index.html                      inlogpagina met de demo AES-versleuteld erin (gaat naar GitHub Pages)

De login staat in login.local (regel 1 gebruikersnaam, regel 2 wachtwoord) en staat niet in git.
"""
import base64, os, pathlib, subprocess

ITER = 150000
d = pathlib.Path(__file__).parent
html = (d / "app.src.html").read_text(encoding="utf-8")
for f in sorted((d / "avatars").glob("*.jpg")):
    html = html.replace(f"__AV_{f.stem}__", "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode())
html = html.replace("/*__LEAFLET_CSS__*/", (d / "vendor/leaflet.css").read_text(encoding="utf-8"))
html = html.replace("/*__LEAFLET_JS__*/", (d / "vendor/leaflet.js").read_text(encoding="utf-8").replace("</script", "<\\/script"))
html = html.replace("/*__ZONES__*/{}", (d / "vendor/zones.json").read_text(encoding="utf-8"))

meta = (d / "head-meta.html").read_text(encoding="utf-8")
head = '<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n' + meta
page = head + html.replace("</style>\n\n<div", "</style>\n</head>\n<body>\n<div", 1) + "\n</body>\n</html>\n"

(d / "local").mkdir(exist_ok=True)
(d / "local" / "LocalBuddy-offline.html").write_text(page, encoding="utf-8")

user, pw = (d / "login.local").read_text(encoding="utf-8").splitlines()[:2]
enc = subprocess.run(
    ["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", str(ITER), "-md", "sha256", "-salt", "-pass", "env:LB_PASS"],
    input=page.encode(), env={**os.environ, "LB_PASS": user.strip().lower() + "\n" + pw},
    capture_output=True, check=True,
).stdout
payload = base64.b64encode(enc).decode()
login = (d / "login.html").read_text(encoding="utf-8").replace("<!--HEADMETA-->", meta)
(d / "index.html").write_text(login.replace("__PAYLOAD__", payload).replace("__ITER__", str(ITER)), encoding="utf-8")
print("offline:", len(page) // 1024, "KB · index.html (versleuteld):", (d / "index.html").stat().st_size // 1024, "KB")
