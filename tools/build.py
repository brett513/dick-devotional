import json,urllib.request,urllib.parse,datetime,time,re
from content import D
drop={"Psalm 19:1","Psalm 145:18","Psalm 92:1-2","John 14:6","John 11:25","1 Corinthians 13:13","Romans 12:12"}
D=[d for d in D if d[0] not in drop]
i=[k for k,d in enumerate(D) if d[0]=="Luke 2:11"][0]
D[i]=("Luke 2:12","The sign of the Savior was a baby wrapped in cloths, lying in a manger. God's greatest gift came in the humblest wrapping. Look for His presence in simple places today.","Lord Jesus, thank You for coming so humbly. Help me find You in simple places. Amen.")
assert len(D)==108
out={};start=datetime.date(2026,10,16)
for k,(ref,refl,pr) in enumerate(D):
    for t in range(5):
        try:
            j=json.load(urllib.request.urlopen("https://bible-api.com/"+urllib.parse.quote(ref)+"?translation=web"));break
        except Exception as e: time.sleep(3)
    txt=re.sub(r'\s+',' '," ".join(v["text"] for v in j["verses"])).strip()
    out[(start+datetime.timedelta(k)).isoformat()]={"reference":j["reference"],"translation":"WEB","verse":txt,"reflection":refl,"prayer":pr}
    time.sleep(1.2)
json.dump(out,open("devotions.json","w"),indent=1,ensure_ascii=False)
print(list(out)[-1], out["2026-10-16"], out["2026-11-26"]["reference"], out["2026-12-25"]["reference"])
