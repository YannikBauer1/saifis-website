import json,re
s=open('index.html',encoding='utf8').read()
def between(a,b,inc=True):
    i=s.index(a); j=s.index(b,i)+(len(b) if inc else 0); return s[i:j]
header=between('<header class="bar is-solid">','</header>').replace('class="bar is-solid"','class="bar"').replace('href="#top"','href="index.html"')
close=between('<!-- Act 8.','</section>').split('\n',1)[1]
foot=between('<footer class="foot on-dark">','</footer>').replace('href="#top"','href="index.html"').replace('href="#ablauf"','href="index.html#ablauf"').replace('href="#bewertungen"','href="index.html#bewertungen"')
dock=between('<div class="dock">','</div>')
dialog=between('<dialog id="anfrage"','</dialog>')
objs=between('<ul class="objs"','</ul>')
def srcsets(h,small=()):
    # Phones get a smaller version of any big photo.
    W={'g-ford':1500,'g-door':1500,'g-facade':1500,'g-hescuro':1500,'g-terrace':1500,'m-van':1000,'m-ladder':1152,'m-window':1599,'ref-jalousie':900,'ref-haufen-befund':900,'ref-boden-befund':780,'ref-kueche-nachher':780,'ref-raum-ergebnis':780,'ref-gofit-glas':720}
    for k,w in W.items():
        extra=f'assets/{k}-800.webp 800w, ' if w>900 or k=='m-van' or k=='ref-jalousie' and False else ''
        sz='(max-width: 860px) 46vw, 34vw' if k in small else '(max-width: 600px) 80vw, (max-width: 860px) 100vw, 45vw'
        h=re.sub(r'(<img(?![^>]*srcset)[^>]*?)src="assets/%s\.webp"'%k, lambda m:f'{m.group(1)}src="assets/{k}.webp" srcset="assets/{k}-420.webp 420w, {extra}assets/{k}.webp {w}w" sizes="{sz}"',h)
    return h
def page(file,title,desc,cur,body,path=None):
    h=header.replace('<a href="%s">'%file,'<a href="%s" aria-current="page">'%file)
    f=foot.replace('<li><a href="%s">'%file,'<li><a href="%s" aria-current="page">'%file)
    html=f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="canonical" href="https://saifis-gebaeudereinigung.de/{path if path is not None else file[:-5]}">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" href="assets/favicon-96.png" sizes="96x96">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/archivo-latin.woff2" crossorigin>
<link rel="stylesheet" href="scrollcraft.css">
<link rel="stylesheet" href="site.css">
<link rel="stylesheet" href="pages.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt</a>

{h}

<main id="inhalt">
{body}
{close}
</main>

{f}

{dock}

{dialog}

<script src="scrollcraft.js" defer></script>
<script src="site.js" defer></script>
</body>
</html>
'''
    html=html.replace('100 %','100&nbsp;%')
    open(file,'w',encoding='utf8').write(srcsets(html, ('g-door','g-facade','g-terrace','g-hescuro','ref-jalousie','ref-gofit-glas','ref-haufen-befund','ref-boden-befund','ref-kueche-nachher','ref-raum-ergebnis') if file=='unsere-arbeit.html' else ()))

# ================================================== Leistungen
G=[('glas-fassade','Glas und Fassade',False,False,'<video data-loop muted playsinline loop preload="none" poster="assets/ref-squeegee.webp" width="720" height="960" style="object-position:50% 8%" aria-label="Mitarbeiter im Saifi\'s-Shirt zieht eine große Scheibe mit dem Abzieher ab."><source src="assets/ref-squeegee.mp4" type="video/mp4"></video>',[
 ('glasreinigung','Glasreinigung','Fenster und Glasflächen.'),
 ('fassadenreinigung','Fassaden&shy;reinigung','Fassaden, ohne bleibende Schäden.'),
 ('photovoltaikreinigung','Photovoltaik&shy;reinigung','Solaranlagen und Module.'),
 ('jalousienreinigung','Jalousien&shy;reinigung','Jalousien und Fensterbänke.'),
 ('steinreinigung','Steinreinigung','Steinflächen und Fugen.'),
 ('graffitientfernung','Graffiti&shy;entfernung','Graffiti an Gebäudeflächen.')]),
('laufend','Laufend im Objekt',True,True,'<img loading="lazy" src="assets/m-ladder.webp" width="1152" height="869" style="object-position:38% 50%" alt="Mitarbeiter im Saifi\'s-Shirt arbeitet auf der Leiter unter einem Holzdach.">',[
 ('unterhaltsreinigung','Unterhalts&shy;reinigung','Ihre Räume, regelmäßig.'),
 ('treppenhausreinigung','Treppenhaus&shy;reinigung','Treppenhäuser und Geländer.'),
 ('desinfektionsreinigung','Desinfektions&shy;reinigung','Keimfreie Räume.'),
 ('hausmeisterservice','Hausmeister&shy;service','Wartung und Reparaturen.')]),
('einmalig','Gründlich und einmalig',False,False,'<img loading="lazy" src="assets/ref-raum-ergebnis.webp" width="780" height="1040" alt="Leerer, frisch gereinigter Raum mit Holzboden.">',[
 ('grundreinigung','Grundreinigung','Alles auf Hochglanz.'),
 ('baureinigung','Baureinigung','Staubfrei nach dem Bau.'),
 ('teppichreinigung','Teppichreinigung','Schmutz, Flecken und Gerüche.'),
 ('polsterreinigung','Polsterreinigung','Polstermöbel, Flecken und Gerüche.')])]
body='''  <section class="page-head">
    <div class="sc-wrap">
      <h1>Leistungen.</h1>
      <p>Gebäudereinigung in Bad Kissingen und Umgebung.</p>
      <ul class="page-jump">'''+''.join(f'<li><a href="#{g[0]}">{g[1]}</a></li>' for g in G)+'''<li><a href="#objekte">Objekte</a></li></ul>
    </div>
  </section>
'''
SUBS={'glas-fassade':'Außen am Gebäude.','laufend':'Regelmäßig, im Abo.','einmalig':'Einmal, dafür sehr intensiv.'}
for gid,name,pale,flip,media,rows in G:
    cl='group'+(' group--pale' if pale else '')+(' group--flip' if flip else '')
    rr=''.join(f"""
          <a class="srow" id="{i}" href="{dict(desinfektionsreinigung='desinfektion',hausmeisterservice='hausmeister-service').get(i,i)}.html"><h3>{n}</h3><p>{t}</p></a>""" for i,n,t in rows)
    body+=f'''
  <section class="{cl}" id="{gid}">
    <div class="sc-wrap group__grid">
      <figure class="group__media">{media}</figure>
      <div data-sc-in>
        <h2>{name}</h2>
        <p class="group__sub">{SUBS[gid]}</p>
        <div class="srows">{rr}
        </div>
      </div>
    </div>
  </section>
'''
body+=f'''
  <section class="page-objs" id="objekte">
    <div class="sc-wrap">
      <h2>Für diese Objekte sind wir unterwegs.</h2>
      {objs.replace(' data-sc-in data-sc-stagger="40"','')}
    </div>
  </section>
'''
page('leistungen.html',"Leistungen: Glas-, Fassaden- und Unterhaltsreinigung | Saifi's","Alle Leistungen in Bad Kissingen und Umgebung: Glasreinigung, Fassadenreinigung, Unterhaltsreinigung, Grundreinigung, Hausmeisterservice und mehr.",'leistungen',body)

# ================================================== Unsere Arbeit
def img(src,w,h,alt,s,ar=None,o=None,pos=None,cap=None,video=None):
    st=f'--s:{s};--ar:{ar or f"{w}/{h}"}'+(f';--o:{o}' if o else '')+(f';--pos:{pos}' if pos else '')
    if video: m=f'<video data-loop muted playsinline loop preload="none" poster="assets/{src}" width="{w}" height="{h}" aria-label="{alt}"><source src="assets/{video}" type="video/mp4"></video>'
    else: m=f'<img loading="lazy" src="assets/{src}" width="{w}" height="{h}" alt="{alt}">'
    c=f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure style="{st}">{m}{c}</figure>'
def job(jid,name,tag,items,pale=False,flip=False,pairs=False,web=None):
    cl='job'+(' job--pale' if pale else '')+(' job--flip' if flip else '')
    return f"""
  <section class="{cl}" id="{jid}">
    <div class="sc-wrap job__grid">
      <div class="job__copy" data-sc-in>
        <h2>{f'<a class="co-link" href="{web}" rel="noopener">{name}</a>' if web else name}</h2>
        <p>{tag}</p>
      </div>
      <div class="job__media{' job__media--pairs' if pairs else ''}{' job__media--trio' if len(items)==3 else ''}">{''.join(items)}</div>
    </div>
  </section>
"""
CLIENTS=[('loeffler','Autohaus Löffler, Ford'),('lebenshilfe','Lebenshilfe Hammelburg'),('gofit','GoFit, Bad Kissingen'),('hescuro','Hescuro'),('weitere','Parkhotel Cup Vitalis, Bad Kissingen'),('weitere','Athera Physio')]
body="""  <section class="page-head">
    <div class="sc-wrap">
      <h1>Unsere Arbeit.</h1>
      <p>Für diese Kunden waren wir in Bad Kissingen und Umgebung im Einsatz.</p>
      <ul class="page-jump">"""+''.join(f'<li><a href="#{a}">{n}</a></li>' for a,n in CLIENTS)+"""</ul>
    </div>
  </section>
"""
body+=job('loeffler','Autohaus Löffler, Ford','Glasreinigung außen: Glasturm, Fensterfront und Sektionaltor.',[
 img('g-ford.webp',1500,1172,'Runder Glasturm eines Autohauses mit Ford-Logo.',7,pos='100% 60%').replace('loading="lazy"','fetchpriority="high"'),
 img('g-door.webp',1500,1171,'Großes verglastes Sektionaltor, in dem sich der Himmel spiegelt.',5,o='clamp(0rem, 4vw, 3.5rem)'),
 img('g-facade.webp',1500,1171,'Lange Fensterfront unter blauem Himmel.',6)],pale=True,web='https://auto-loeffler.de/')
body+=job('lebenshilfe','Lebenshilfe Hammelburg','Glas und Fassade, auch mit Teleskopstange und Wasserzufuhr.',[
 img('ref-squeegee.webp',720,960,"Mitarbeiter im Saifi's-Shirt zieht eine große Scheibe mit dem Abzieher ab.",7,pos='50% 22%',video='ref-squeegee.mp4'),
 img('ref-jalousie.webp',900,1200,'Lange Gebäudefront mit Jalousien neben einem gepflasterten Weg.',5,o='clamp(0rem, 5vw, 4rem)')],flip=True)
body+=job('gofit','GoFit, Bad&nbsp;Kissingen','Eingangstüren und Fenster im Fitnessstudio in Bad Kissingen.',[
 img('gofit-door.webp',848,480,'Glastüren am Eingang des Fitnessstudios GoFit, daneben das Schild mit Logo.',8,video='gofit-door.mp4'),
 img('ref-gofit-glas.webp',720,1280,'Mitarbeiter auf der Leiter reinigt ein hohes Glasdach von innen.',4,ar='3/4',pos='50% 70%')],pale=True,web='https://www.gofit-badkissingen.de/')
body+=job('hescuro','Hescuro','Glasreinigung, auch in der Höhe mit Sicherheitsgurt.',[
 img('ref-harness.webp',764,576,'Mitarbeiter mit Sicherheitsgurt reinigt eine Scheibe hoch über der Stadt.',7,video='ref-harness.mp4'),
 img('g-terrace.webp',1500,1132,'Überdachte Glasterrasse vor Bäumen.',5,o='clamp(0rem, 4vw, 3.5rem)'),
 img('g-hescuro.webp',1500,1132,'Vordach mit Schriftzug Hescuro vor blauem Himmel.',7)],flip=True,web='https://www.hescuro.de/')
body+=job('wohnung','Komplett&shy;reinigung einer Wohnung','Vorher und nachher, aus demselben Einsatz.',[
 img('ref-haufen-befund.webp',900,1200,'Müllsäcke und Abfall auf dem Boden eines Zimmers.',6,ar='4/3',cap='Vorher'),
 img('ref-boden-befund.webp',780,1040,'Holzboden voller Schutt und Abfall.',6,ar='4/3',cap='Vorher'),
 img('ref-kueche-nachher.webp',780,1040,'Gereinigte, leere Küche mit Fenster.',6,ar='4/3',pos='50% 40%',cap='Nachher'),
 img('ref-raum-ergebnis.webp',780,1040,'Leerer, frisch gereinigter Raum mit Holzboden.',6,ar='4/3',pos='50% 60%',cap='Nachher')],pale=True,pairs=True)
def more(src,w,h,alt,name,tag,video,web=None):
    m=f'<video data-loop muted playsinline loop preload="none" poster="assets/{src}" width="{w}" height="{h}" aria-label="{alt}"><source src="assets/{video}" type="video/mp4"></video>'
    return f"""
        <figure>{m}<figcaption><b>{f'<a class="co-link" href="{web}" rel="noopener">{name}</a>' if web else name}</b><span>{tag}</span></figcaption></figure>"""
body+=f"""
  <section class="more" id="weitere">
    <div class="sc-wrap">
      <h2>Weitere Einsätze.</h2>
      <div class="more__grid">{more('ref-cupitalis.webp',480,854,'Mitarbeiter reinigt mit der Teleskopstange eine verglaste Brücke zwischen zwei Gebäuden.','Parkhotel Cup Vitalis, Bad Kissingen','Glasreinigung mit Teleskopstange','ref-cupitalis.mp4','https://www.cupvitalis.de/')}{more('ref-athera.webp',360,480,'Teleskopstange an der Fensterfront über dem Schild von Athera Physio.','Athera Physio','Fensterreinigung mit Teleskopstange','ref-athera.mp4','https://athera.info/')}{more('ref-solar.webp',360,480,'Bürste reinigt Solarmodule auf einem Dach.','Solaranlage','Photovoltaikreinigung','ref-solar.mp4')}
      </div>
    </div>
  </section>
"""
page('unsere-arbeit.html',"Unsere Arbeit: Einsätze in Bad Kissingen und Umgebung | Saifi's","Für diese Kunden waren wir im Einsatz: Autohaus Löffler, Lebenshilfe Hammelburg, GoFit Bad Kissingen, Parkhotel Cup Vitalis, Hescuro und mehr.",'arbeit',body)

# ================================================== Service pages, at the old addresses
AREA=['Bad Kissingen','Schweinfurt','Würzburg','Fulda','Bamberg','Lohr am Main','Karlstadt','Kitzingen','Gelnhausen','Suhl']
SERVICES=[
 ('glasreinigung','Glasreinigung','Fenster und Glasflächen in Bad Kissingen und Umgebung.','Ihre Fenster bleiben dauerhaft sauber, damit Kunden, Mitarbeiter und Lieferanten stets klaren Durchblick haben. Auch hohe Scheiben erreichen wir, mit Teleskopstange und Wasserzufuhr.',['Saubere Fensterrahmen','Keine Streifen auf den Scheiben','Keine Schäden an der Oberfläche'],'m-window',1599,1248,'Blick durch ein sauberes Sektionaltor in den blauen Himmel.'),
 ('fassadenreinigung','Fassadenreinigung','Saubere Fassaden in Bad Kissingen und Umgebung.','Sieht Ihre Fassade nicht mehr wie neu aus? Streichen oder reinigen: Was die bessere Lösung ist, klären wir im Analyse-Termin. So bleibt der Wert Ihrer Immobilie erhalten.',['Kein bleibender Schmutz','Mit Auffangsystem','Das Schmutzwasser bleibt nicht zurück'],'g-facade',1500,1171,'Lange Fensterfront unter blauem Himmel.'),
 ('photovoltaikreinigung','Photovoltaikreinigung','Saubere Solaranlagen in Bad Kissingen und Umgebung.','Verschmutzungen beeinträchtigen die Energieeffizienz Ihrer Anlage. Wir reinigen die Module, damit Sie das volle Potenzial an Strom gewinnen können.',['Keine ungereinigten Stellen','Anhaltender Schutz','Keine Schäden an der Oberfläche'],'ref-solar',360,480,'Bürste reinigt Solarmodule auf einem Dach.'),
 ('jalousienreinigung','Jalousienreinigung','Saubere Jalousien in Bad Kissingen und Umgebung.','Bei Jalousien kommt es auf Gründlichkeit und das richtige Werkzeug an. So fühlen sich Kunden, Mitarbeiter und Lieferanten bei Ihnen wohl.',['Ohne Schmutz und Flecken','Auch die Fensterbank','Keine Schäden an der Oberfläche'],'ref-jalousie',900,1200,'Lange Gebäudefront mit Jalousien neben einem gepflasterten Weg.'),
 ('steinreinigung','Steinreinigung','Saubere Steinflächen in Bad Kissingen und Umgebung.','Sehen Ihre Steine nicht mehr wie neu aus? Wir reinigen sie gründlich und mit dem richtigen Equipment, damit Ihre Immobilie wieder im vollen Glanz erscheint.',['Kein Dreck in den Fugen','Keine Flecken','Keine Schäden an der Oberfläche'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
 ('graffitientfernung','Graffitientfernung','Graffiti entfernen in Bad Kissingen und Umgebung.','Neue Graffiti an Ihrem Gebäude? Wir entfernen sie so, dass keine Spur übrig bleibt und die Fläche darunter nicht leidet.',['Keine Überreste','Keine beschädigten Oberflächen','Professionelle Technik'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
 ('unterhaltsreinigung','Unterhaltsreinigung','Regelmäßige Reinigung in Bad Kissingen und Umgebung.','Im Reinigungsabo bleibt Ihr Gebäude dauerhaft sauber, damit sich Kunden, Mitarbeiter und Lieferanten wohlfühlen. Wir prüfen die Qualität regelmäßig und unangekündigt.',['Keine verstaubten Oberflächen','Keine Griffspuren an Türen','Keine Schäden an der Oberfläche'],'m-ladder',1152,869,"Mitarbeiter im Saifi's-Shirt arbeitet auf der Leiter unter einem Holzdach."),
 ('treppenhausreinigung','Treppenhausreinigung','Saubere Treppenhäuser in Bad Kissingen und Umgebung.','Im Reinigungsabo bleibt Ihr Treppenhaus dauerhaft sauber, damit sich Mieter wohlfühlen und Ihre Immobilie ihren Wert hält.',['Saubere Ecken','Keine Griffspuren am Geländer','Keine Schäden an der Oberfläche'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
 ('desinfektion','Desinfektionsreinigung','Keimfreie Räume in Bad Kissingen und Umgebung.','Bei der Desinfektion zählt die umfassende Entfernung von Keimen und Bakterien. Wir sorgen für konstante und keimfreie Sauberkeit in Ihren Räumlichkeiten.',['Keine Staubreste und Flecken','Gründliche Reinheit','Keine Schäden an der Oberfläche'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
 ('hausmeister-service','Hausmeisterservice','Hausmeister für Ihr Gebäude in Bad Kissingen und Umgebung.','Wir koordinieren und erledigen Wartungsarbeiten und Reparaturen, damit Ihr Gebäude konstant in Stand bleibt und sich Kunden, Mitarbeiter und Bewohner wohlfühlen.',['Saubere Treppen','Sauberer Kellerbereich','Keine Schäden an der Oberfläche'],'m-ladder',1152,869,"Mitarbeiter im Saifi's-Shirt arbeitet auf der Leiter unter einem Holzdach."),
 ('grundreinigung','Grundreinigung','Einmal gründlich, in Bad Kissingen und Umgebung.','Manchmal braucht es eine einmalige, dafür sehr intensive Reinigung. Wir bringen Ihre Räumlichkeiten auf Hochglanz.',['Saubere Flächen','Die richtige Reinigungstechnik','Zu einem fairen Preis'],'ref-raum-ergebnis',780,1040,'Leerer, frisch gereinigter Raum mit Holzboden.'),
 ('baureinigung','Baureinigung','Reinigung nach dem Bau, in Bad Kissingen und Umgebung.','Wir sorgen für staubfreie Sauberkeit auf Ihrer Baustelle, damit sich Kunden, Mitarbeiter und Gewerke wohlfühlen, und halten dabei Sicherheits- und Qualitätsstandards ein.',['Saubere Oberflächen','Bauschutt wird entsorgt','Keine Schäden an der Oberfläche'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
 ('teppichreinigung','Teppichreinigung','Saubere Teppiche in Bad Kissingen und Umgebung.','Sieht Ihr Teppich nicht mehr wie neu aus? Wir reinigen ihn gründlich und mit dem richtigen Werkzeug, ohne bleibende Schäden.',['Ohne Schmutz und Flecken','Kein unangenehmer Geruch','Keine Schäden an der Oberfläche'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
 ('polsterreinigung','Polsterreinigung','Saubere Polstermöbel in Bad Kissingen und Umgebung.','Flecken und Gerüche hinterlassen ein unangenehmes Gefühl. Wir reinigen Ihre Polstermöbel, ohne dass bleibende Schäden entstehen.',['Ohne Schmutz und Flecken','Keine negativen Gerüche','Keine Schäden an der Oberfläche'],'m-van',1000,1333,"Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."),
]
FAQ=[('Bekomme ich einen festen Ansprechpartner?','Ja. Sie erhalten einen festen Ansprechpartner bei uns im Haus, der Ihnen persönlich, telefonisch oder per E-Mail zur Verfügung steht. Zudem teilen wir Ihnen einen Objektleiter direkt vor Ort zu.'),
('Sind Sie versichert?','Ja. Wir sind über eine umfassende Betriebshaftpflicht, eine Schlüsselversicherung sowie eine Versicherung gegen Bearbeitungsschäden versichert.'),
('Wie kommt der Preis zustande?','Wir kalkulieren unsere Angebote immer individuell, passend zu Ihren Bedürfnissen und Ihrem Objekt. Der Analyse-Termin ist kostenfrei und 100 % unverbindlich.'),
('Wie kontrollieren Sie die Qualität?','Unsere Projektleiter vor Ort führen regelmäßige Qualitätskontrollen durch, und alle erbrachten Leistungen dokumentieren wir sorgfältig.')]
def faq_html():
    return '<section class="faq"><div class="sc-wrap"><h2>Häufige Fragen.</h2>'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)+'</div></section>'
TEL_ICON='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
def cta(prefill=''):
    return f'<div class="sv-cta"><a class="btn btn--termin" href="mailto:info@saifis-gebaeudereinigung.de" data-anfrage{prefill}>Analyse-Termin anfragen</a><a class="btn btn--tel" href="tel:+4997112382990">{TEL_ICON}0971 12382990</a></div>'
def service_ld(name,slug,area):
    a=json.dumps(area,ensure_ascii=False)
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{name}","url":"https://saifis-gebaeudereinigung.de/{slug}","areaServed":{a},"provider":{{"@type":"LocalBusiness","@id":"https://saifis-gebaeudereinigung.de/#business","name":"Saifi\'s Gebäudereinigung","telephone":"+4997112382990","address":{{"@type":"PostalAddress","streetAddress":"Prinzregentenstraße 3","postalCode":"97688","addressLocality":"Bad Kissingen","addressCountry":"DE"}}}}}}</script>'
GROUPS=[('Glas und Fassade',SERVICES[:6]),('Laufend im Objekt',SERVICES[6:10]),('Gründlich und einmalig',SERVICES[10:])]
def more_services(skip=None):
    out=''
    for h,items in GROUPS:
        out+=f'<div><h3>{h}</h3><ul>'+''.join(f'<li><a class="pick" href="{s[0]}.html">{s[1]}</a></li>' for s in items if s[0]!=skip)+'</ul></div>'
    return out
for slug,name,sub,text,bullets,im,w,h_,alt in SERVICES:
    source=f'assets/{im}.webp'
    body=f"""  {service_ld(name,slug,AREA)}
  <section class="page-head sv-head">
    <div class="sc-wrap sv-grid">
      <div>
        <h1>{re.sub(r'(reinigung|entfernung|service)$',r'&shy;\1',name)}<br>in Bad&nbsp;Kissingen</h1>
        <p>{sub}</p>
        <p class="sv-text">{text}</p>
        <ul class="sv-list">{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
        {cta(f' data-leistung="{name}"')}
      </div>
      <figure class="sv-photo"><img fetchpriority="high" src="{source}" width="{w}" height="{h_}" alt="{alt}"></figure>
    </div>
  </section>
  <section class="sv-more">
    <div class="sc-wrap">
      <h2>Weitere Leistungen.</h2>
      <div class="svcs">{more_services(slug)}</div>
    </div>
  </section>
  {faq_html()}
"""
    page(f'{slug}.html',f"{name} Bad Kissingen | Saifi's Gebäudereinigung",f"{name} in Bad Kissingen und Umgebung. Kostenfreier Analyse-Termin, persönlicher Ansprechpartner, 5,0 auf Google.",'svc',body,path=slug)

# ================================================== Town pages
CITIES=[
 dict(slug='gebaeudereinigung-schweinfurt',town='Schweinfurt',title="Gebäudereinigung Schweinfurt | Saifi's Gebäudereinigung",
  desc='Gebäudereinigung und Reinigungsfirma für Schweinfurt: Fensterreinigung, Unterhaltsreinigung und Hausmeisterservice. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Schweinfurt',sub='Ihre Reinigungsfirma aus Bad Kissingen, auch in Schweinfurt im Einsatz.',
  text='Fensterreinigung, Glas- und Fassadenreinigung, Unterhaltsreinigung und Hausmeisterservice für Betriebe und Hausverwaltungen in Schweinfurt. Inhabergeführt, mit persönlichem Ansprechpartner und eigenen Qualitätskontrollen.',
  more='Leistungen in Schweinfurt.'),
 dict(slug='gebaeudereinigung-wuerzburg',town='Würzburg',title="Gebäudereinigung & Reinigungsfirma Würzburg | Saifi's",
  desc='Reinigungsfirma für Würzburg: Gebäudereinigung, Fenster- und Glasreinigung, Unterhaltsreinigung und Hausmeisterservice. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Würzburg',sub='Saifi\'s ist Ihre inhabergeführte Reinigungsfirma für Würzburg.',
  text='Sie suchen eine Reinigungsfirma in Würzburg, die Absprachen einhält? Wir reinigen Glas, Fassaden und Treppenhäuser, übernehmen die laufende Unterhaltsreinigung und den Hausmeisterservice. Der Inhaber steht persönlich dafür ein, und unser eigenes Q-Check-System prüft die Qualität unangekündigt.',
  more='Das übernehmen wir in Würzburg.'),
 dict(slug='gebaeudereinigung-fulda',town='Fulda',title="Gebäudereinigung Fulda | Saifi's Gebäudereinigung",
  desc='Gebäudereinigung für Fulda: Glas- und Fassadenreinigung, Unterhaltsreinigung und Hausmeisterservice. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Fulda',sub='Ein persönlicher Ansprechpartner für Ihr Gebäude in Fulda.',
  text='Für Betriebe und Hausverwaltungen in Fulda übernehmen wir die Glas- und Fassadenreinigung, die laufende Unterhaltsreinigung und den Hausmeisterservice. Vor dem Angebot sehen wir uns Ihr Objekt an, danach haben Sie einen festen Ansprechpartner.',
  more='Unsere Leistungen in Fulda.'),
 dict(slug='gebaeudereinigung-bamberg',town='Bamberg',title="Gebäudereinigung & Reinigungsfirma Bamberg | Saifi's",
  desc='Reinigungsfirma für Bamberg: Gebäude-, Glas- und Unterhaltsreinigung sowie Hausmeisterservice. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Bamberg',sub='Ihre Reinigungsfirma für Bamberg, mit einem festen Ansprechpartner.',
  text='Zuverlässige Termine und klare Absprachen: Für Betriebe und Hausverwaltungen in Bamberg übernehmen wir die Gebäude- und Glasreinigung, die regelmäßige Unterhaltsreinigung und den Hausmeisterservice.',
  more='Unsere Leistungen in Bamberg.'),
 dict(slug='gebaeudereinigung-lohr',town='Lohr am Main',title="Gebäudereinigung Lohr am Main | Saifi's Gebäudereinigung",
  desc='Gebäudereinigung für Lohr am Main: Fenster- und Glasreinigung, Treppenhausreinigung und Hausmeisterservice. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Lohr am Main',sub='Saubere Gebäude in Lohr am Main, vom inhabergeführten Betrieb.',
  text='Von der Fensterreinigung bis zum Hausmeisterservice: In Lohr am Main reinigen wir Glasflächen und Treppenhäuser und halten Ihr Objekt laufend in Schuss. Ihr Angebot kalkulieren wir individuell, nachdem wir Ihr Objekt gesehen haben.',
  more='Das reinigen wir in Lohr am Main.'),
 dict(slug='gebaeudereinigung-karlstadt',town='Karlstadt',title="Gebäudereinigung Karlstadt | Saifi's Gebäudereinigung",
  desc='Gebäudereinigung für Karlstadt: Unterhalts-, Treppenhaus- und Grundreinigung für Betriebe und Hausverwaltungen. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Karlstadt',sub='Regelmäßig oder einmalig: Reinigung für Ihr Objekt in Karlstadt.',
  text='Ob laufende Unterhaltsreinigung, gepflegtes Treppenhaus oder eine einmalige Grundreinigung: In Karlstadt stimmen wir den Plan auf Ihr Objekt ab. Unsere Projektleiter kontrollieren die Qualität regelmäßig und dokumentieren die Leistungen.',
  more='Unsere Leistungen in Karlstadt.'),
 dict(slug='gebaeudereinigung-kitzingen',town='Kitzingen',title="Gebäudereinigung & Reinigungsfirma Kitzingen | Saifi's",
  desc='Reinigungsfirma für Kitzingen: Gebäudereinigung, Glas- und Fassadenreinigung und Baureinigung. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Kitzingen',sub='Glas, Fassade und Innenräume: alles von einer Reinigungsfirma.',
  text='In Kitzingen übernehmen wir die Glas- und Fassadenreinigung ebenso wie die Reinigung Ihrer Innenräume oder die Baureinigung. Sie haben einen festen Ansprechpartner bei uns und einen Objektleiter vor Ort.',
  more='Das übernehmen wir in Kitzingen.'),
 dict(slug='gebaeudereinigung-gelnhausen',town='Gelnhausen',title="Gebäudereinigung Gelnhausen | Saifi's Gebäudereinigung",
  desc='Gebäudereinigung für Gelnhausen: Glasreinigung, Unterhaltsreinigung und Hausmeisterservice für Betriebe. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Gelnhausen',sub='Ein Betrieb für Reinigung und Hausmeisterservice in Gelnhausen.',
  text='Weniger Abstimmung, ein Partner: In Gelnhausen übernehmen wir für Sie Glasreinigung, Unterhaltsreinigung und Hausmeisterservice. Wir sind über Betriebshaftpflicht, Schlüsselversicherung und gegen Bearbeitungsschäden versichert.',
  more='Unsere Leistungen in Gelnhausen.'),
 dict(slug='gebaeudereinigung-suhl',town='Suhl',title="Gebäudereinigung & Reinigungsfirma Suhl | Saifi's",
  desc='Reinigungsfirma für Suhl: Gebäudereinigung, Unterhaltsreinigung und Photovoltaikreinigung. Kostenfreier Analyse-Termin, 5,0 auf Google.',
  h1='Gebäudereinigung in Suhl',sub='Ihre Reinigungsfirma für Suhl und Umgebung.',
  text='Für Objekte in Suhl bieten wir die regelmäßige Unterhaltsreinigung genauso wie Spezialreinigungen an, etwa von Fassaden oder Photovoltaikanlagen. Der Analyse-Termin vor Ort ist kostenfrei und unverbindlich.',
  more='Unsere Leistungen in Suhl.'),
]
for c in CITIES:
    body=f"""  {service_ld(c['h1'].replace(' in ',' '),c['slug'],[c['town']])}
  <section class="page-head sv-head">
    <div class="sc-wrap sv-grid">
      <div>
        <h1>{c['h1'].replace(' in ','<br>in ',1)}</h1>
        <p>{c['sub']}</p>
        <p class="sv-text">{c['text']}</p>
        <ul class="sv-list"><li>Analyse-Termin kostenfrei und 100 % unverbindlich</li><li>Angebot individuell für Ihr Objekt</li><li>5,0 auf Google, 42 Bewertungen</li></ul>
        {cta(f''' data-leistung="{c['h1']}"''')}
      </div>
      <figure class="sv-photo"><img fetchpriority="high" src="assets/m-van.webp" width="1000" height="1333" alt="Saifi's Transporter mit Logo und dem Schriftzug Sauber. Schnell. Zuverlässig."></figure>
    </div>
  </section>
  <section class="sv-more">
    <div class="sc-wrap">
      <h2>{c['more']}</h2>
      <div class="svcs">{more_services()}</div>
    </div>
  </section>
  {faq_html()}
"""
    page(c['slug']+'.html',c['title'],c['desc'],'city',body,path=c['slug'])

# ================================================== Einsatzgebiet
REGIONS=[('Bad Kissingen und Rhön',[('Bad Kissingen','index.html'),('Hammelburg','unsere-arbeit.html#lebenshilfe'),('Münnerstadt',None),('Bad Brückenau',None),('Bad Neustadt',None),('Bad Königshofen',None),('Mellrichstadt',None)]),
 ('Schweinfurt und Haßberge',[('Schweinfurt','gebaeudereinigung-schweinfurt.html'),('Haßfurt',None),('Gerolzhofen',None),('Volkach',None)]),
 ('Würzburg und Main',[('Würzburg','gebaeudereinigung-wuerzburg.html'),('Kitzingen','gebaeudereinigung-kitzingen.html'),('Ochsenfurt',None),('Karlstadt','gebaeudereinigung-karlstadt.html'),('Gemünden',None),('Lohr am Main','gebaeudereinigung-lohr.html'),('Marktheidenfeld',None),('Wertheim',None)]),
 ('Fulda und Osthessen',[('Fulda','gebaeudereinigung-fulda.html'),('Hünfeld',None),('Schlüchtern',None),('Gelnhausen','gebaeudereinigung-gelnhausen.html')]),
 ('Thüringen und Oberfranken',[('Meiningen',None),('Suhl','gebaeudereinigung-suhl.html'),('Bamberg','gebaeudereinigung-bamberg.html')])]
regions=''
for h,towns in REGIONS:
    regions+=f'<div><h3>{h}</h3><ul>'+''.join(f'<li><a class="pick" href="{u}">{t}</a></li>' if u else f'<li><span class="pick pick--plain">{t}</span></li>' for t,u in towns)+'</ul></div>'
body=f"""  <section class="page-head">
    <div class="sc-wrap">
      <h1>Einsatzgebiet.</h1>
      <p>Gebäudereinigung in Bad Kissingen und bis zu rund einer Stunde Fahrt darum herum.</p>
      <div class="sv-cta">{cta(' data-leistung="Mein Ort: "').replace('<div class="sv-cta">','',1)[:-6]}</div>
    </div>
  </section>
  <section class="sv-more">
    <div class="sc-wrap">
      <h2>Hier sind wir für Sie im Einsatz.</h2>
      <div class="svcs">{regions}<p class="hub-note">Ihr Ort fehlt? Rufen Sie uns an, wir klären es direkt.</p></div>
    </div>
  </section>
  <section class="sv-more hub-svc">
    <div class="sc-wrap">
      <h2>Das übernehmen wir.</h2>
      <div class="svcs">{more_services()}</div>
    </div>
  </section>
  {faq_html()}
"""
page('einsatzgebiet.html',"Einsatzgebiet: Gebäudereinigung rund um Bad Kissingen | Saifi's","Gebäudereinigung in Bad Kissingen, Schweinfurt, Würzburg, Fulda, Bamberg und Umgebung. Kostenfreier Analyse-Termin, 5,0 auf Google.",'hub',body)

# ================================================== Sitemap
paths=['','leistungen','unsere-arbeit','einsatzgebiet']+[c['slug'] for c in CITIES]+[s[0] for s in SERVICES]
open('sitemap.xml','w',encoding='utf8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>https://saifis-gebaeudereinigung.de/{p}</loc></url>\n' for p in paths)+'</urlset>\n')
