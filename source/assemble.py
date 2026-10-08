"""Inject content.json into the template. Writes the artifact preview and a deployable dist/."""
import json, shutil, os
t = open("template.html").read()
c = json.dumps(json.load(open("content.json")), ensure_ascii=False).replace("</", "<\\/")
page = t.replace("__CONTENT__", c)
open("artifact.html", "w").write(page)
os.makedirs("dist", exist_ok=True)
head, body = page.split("</style>", 1)
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
open("dist/index.html", "w").write(doc)
if os.path.exists("dist/img"): shutil.rmtree("dist/img")
shutil.copytree("img", "dist/img")
print("ok", len(page)//1024, "KB")
