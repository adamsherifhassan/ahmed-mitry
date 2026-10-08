"""Pull published content from Hygraph, download optimised images, write content.json."""
import json, subprocess, urllib.parse
API = "https://eu-central-1.cdn.hygraph.com/content/ckzxa32ec4eu101xnfr106gzw/master"
Q = """{ projects(first:200, orderBy: createdAt_DESC){ id title videoUrl type clientLogo{ url } thumbnail{ url } }
 bioSteps(first:1, orderBy: createdAt_ASC){ image{ url } } }"""
def gql(q):
    out = subprocess.run(["curl","-s","-X","POST",API,"-H","Content-Type: application/json","-d",json.dumps({"query":q})],capture_output=True,text=True).stdout
    return json.loads(out)["data"]
def transform(url, t):
    base, handle = url.rsplit("/",1)
    return f"{base}/{t}/{handle}"
def dl(url, path):
    subprocess.run(["curl","-s","-o",path,url],check=True)

d = gql(Q)
def platform(u):
    h = urllib.parse.urlparse(u.strip()).netloc
    if "youtube" in h: return "YouTube", "Watch"
    if "instagram" in h: return "Instagram", "Watch"
    if "kerningcultures" in h: return "Kerning Cultures", "Listen"
    return h, "Watch"
work = []
for i, p in enumerate(d["projects"]):
    url = (p["videoUrl"] or "").strip()
    title = " ".join(p["title"].split())
    if "kerningcultures.com" in url and "B'Hob" in title:
        slug = urllib.parse.unquote(url.rstrip("/").rsplit("/",1)[1]).replace("-"," ")
        title = f"{title} · {slug}"
    plat, verb = platform(url) if url else ("", "")
    thumb = ""
    if p["thumbnail"]:
        thumb = f"img/work/{p['id']}.jpg"
        dl(transform(p["thumbnail"]["url"], "resize=width:720,fit:max/output=format:jpg"), thumb)
    logo = None
    if p["clientLogo"]:
        logo = f"img/logo-{p['id']}.png"
        dl(transform(p["clientLogo"]["url"], "resize=height:160,fit:max/output=format:png"), logo)
    work.append({"id":p["id"],"title":title,"url":url,"type":p["type"],"platform":plat,"verb":verb,"thumb":thumb,"logo":logo})
# The only photograph on the page: the first bio step's image, used as the hero
hero = "img/hero.jpg"
dl(transform(d["bioSteps"][0]["image"]["url"], "resize=width:1600,fit:max/output=format:jpg"), hero)
json.dump({"work":work,"hero":hero}, open("content.json","w"), ensure_ascii=False, indent=1)
print(len(work), "projects + hero image")
