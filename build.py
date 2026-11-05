import base64, pathlib
d = pathlib.Path(__file__).parent
html = (d / "app.src.html").read_text(encoding="utf-8")
for f in sorted((d / "avatars").glob("*.jpg")):
    uri = "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()
    html = html.replace(f"__AV_{f.stem}__", uri)
# artifact.html: fragment for publishing (the host adds doctype/head)
(d / "artifact.html").write_text(html, encoding="utf-8")
# index.html: standalone offline version
head = '<!doctype html>\n<html lang="nl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
(d / "index.html").write_text(head + html.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n</body>\n</html>\n", encoding="utf-8")
(d / "deploy").mkdir(exist_ok=True)
(d / "deploy" / "index.html").write_text((d / "index.html").read_text(encoding="utf-8"), encoding="utf-8")
print("built", len(html) // 1024, "KB")
