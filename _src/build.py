#!/usr/bin/env python3
"""Builds the static jeonseongjae.com site into ../site from content in this folder.
Edit album.json or the CV/HOME blocks below, then run:  python3 src/build.py"""
import json, html, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT.parent
SITE = "https://www.jeonseongjae.com"

def A(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'

HONGIK = "https://www.hongik.ac.kr/kr/index.do"; SEOULTECH = "https://www.seoultech.ac.kr/"
SUWON = "https://www.suwon.ac.kr/"; KT = "http://koreantypography.org/"; KOSMA = "http://kos-ma.org"
DD = "https://studio-d-d.com/kr"; APS = "https://www.galleryapspace.com/"; MC = "https://www.mattiacasalegno.net/"
PRATT = "https://www.pratt.edu/"; NUPIP = "http://nupip.co.kr/"
KDAILY = "https://news.koreadaily.com/2022/12/18/society/community/20221218183900468.html"

# ---------------- CV (one string per line, "" = blank line) ----------------
def H(t, en=False):
    return f'<u class="h">{t}</u>' if en else f"<u>{t}</u>"

CV_KO = [
 H("작업 영역"), "", "모션그래픽, 3D, 생성형 인공지능, 인터랙티브 아트 설치, AR/MR/VR", "",
 H("주요 경력"), "",
 A(SEOULTECH, "現 ") + A(HONGIK, "홍익대학교, ") + A(SEOULTECH, "서울과학기술대학교, ") + A(SUWON, "수원대학교 | 대학 강의"),
 "現 " + A(KT, "한국타이포그라피학회") + A(KT, " | ") + "사무국장",
 "現 " + A(KOSMA, "한국영상학회") + A(KOSMA, " | ") + "전시운영이사",
 "前 " + A(DD, "더블디") + " | 시니어 디자이너",
 "前 뉴욕 첼시 " + A(APS, "갤러리 AP Space") + " | 디자이너",
 "前 뉴욕 " + A(MC, "Mattia Casalegno Studio") + " | 디자이너", "",
 H("학력"), "",
 "시각디자인 박사과정 / " + A(HONGIK, "홍익대학교"),
 "디지털 아트 석사(수석 졸업) / " + A(PRATT, "프랫 인스티튜트(Pratt Institute)"),
 "시각디자인 학사 / " + A(SEOULTECH, "서울과학기술대학교"), "",
 H("주요 프로젝트"), "",
 "2026 국립현대미술관 과천관 40주년 프로젝트: 빛의 상상들 모션그래픽 디자인",
 "2025 N" + A(NUPIP, "upip") + " 웹사이트 디자인 프로젝트 매니징",
 "2025 HYBE 위버스 매거진 인터랙티브 콘텐츠 'My K-pop Scrapbook' 디자인 및 프로젝트 매니징",
 "2025 TCC스틸 웹사이트 리뉴얼 디자인 프로젝트 매니징",
 "2024 기아 오토랜드 광명 아나모픽 미디어 기획 및 모션그래픽 디자인",
 "2022 이탈리아 베니스 Il Teatro Verde ‘La Maschera del Tempo’ 디자인",
 "2021 기아 디자인 매거진 웹사이트 3D 모션그래픽 디자인",
 "2021 한국문화예술위원회 ‘보이지 않는 도시들’ 웹사이트 모션그래픽 디자인",
 "2021 데이즈드 코리아 Aespa × GIVENCHY 컨셉필름 모션그래픽 디자인",
 "2020 한국공예·디자인문화진흥원 ‘사물과의 대화: 시적인 순간’ 모션그래픽 디자인",
 "2020 쇼크에듀 홀로그램 쇼, 아트디렉팅",
 "2020 아르코미술관 ‘슈퍼 퓨처 푸드’ 모션그래픽 디자인",
 "2019 서울과학기술대학교 졸업전시 인터랙티브 월 디자인",
 "2019 건국대학교 의상디자인학과 졸업전시 영상 아트디렉팅",
 "2019 프랑스 ‘Festival Du Film De La Francophonie’ 모션그래픽 디자인",
 "2018 국제 타이포그래피 비엔날레 ‘타이포잔치 사이사이’ 모션그래픽 디자인",
 "2018 평창올림픽 ‘열정의 노래’ 공연 모션그래픽 디자인",
 "2018 Rebel9 ‘경기도 기억, 기억의 도서관’ 모션그래픽 모션그래픽 디자인",
 "2018 과천국립과학관 인터랙티브 체험 모션그래픽 디자인",
 "2018 국립국악원 인터랙티브 체험 모션그래픽 디자인",
 "2017 국제 타이포그래피 비엔날레 ’타이포잔치' 웹사이트 모션그래픽 디자인",
 "2017 Rebel9 ‘타이포노테이션’ 인터랙티브 월 모션그래픽 디자인",
 "2017 오아 에이전시 그림도시 서울/부산 기획, 디자인 및 운영 참여", "",
 H("전시&amp;영화제"), "",
 "2026 그룹전 '생성과 창작 사이', 홍익대학교 AI뮤지엄",
 "2026 AMCA MBC C&amp;I AI 필름 페스티벌, 서울영화센터",
 "2025 한중예술교류전, 중국 동관시 광동과기대학교",
 "2025 서울로미디어캔버스 KOSMA 봄 국제초대전 '빛결'",
 "2023 그룹전 'Art &amp; Technology', 원 아트 스페이스 뉴욕",
 "2022 FIT&amp;Pratt 연합전 'Kickoff', 미즈마&amp;킵스 갤러리 뉴욕 " + A(KDAILY, "(관련기사)"),
 "2022 Untitled Art Fair, 플로리다 마이애미",
 "2021 그룹전 'Gaea: A garden of the 2nd and 3rd Dimensions', 마이카 브루클린",
 "2021 프랫 인스티튜트 그룹전 'Hello, World!', 브루클린",
 "2021 개인전 '하늘과 땅, 그리고 실재하는 X', 갤러리 유기체",
 "2020 그룹전 '전염과 면역', 두성종이 인더페이퍼갤러리",
 "2018 3인전 'OF', 갤러리 오브",
 "2017 서울디자인위크 EP.age, 동대문디자인플라자",
 "2016 그룹전 'Debut', 동대문디자인플라자", "",
 H("강의"), "",
 "2026 서울과학기술대학교 시각디자인학과 3D미디어디자인, 디지털비디오프로덕션 강의",
 "2026 수원대학교 커뮤니케이션디자인학과 영상디자인, Digital Design3 강의",
 "2026 홍익대학교 시각디자인학과 영상(1), 영상(2) 강의",
 "2025 서울과학기술대학교 디자인학과 시각디자인전공 특강",
 "2025 홍익대학교 시각디자인학과 특강",
 "2024 서울과학기술대학교 디자인학과 시각디자인전공 특강", "",
 H("활동"), "",
 "2023 Pratt Institute 커뮤니케이션 디자인 학부에서 아티스트 토크",
 "2022 삼성디자인멤버십 프로젝트 전시 《Groovy Grove》 튜터",
 "2021 서울로 미디어 캔버스 시민전 심사위원",
 "2019 서울로 미디어 캔버스 시민전 심사위원",
 "2018 오픈 토크 세미나",
 "2017 서울디자인위크 \"더 나은 관계를 위한 디자인\" 청년 디자이너 선정",
]

def plain(lines): return [html.escape(l, quote=False) for l in lines]

CV_EN = [
 H("Work Scope", True), "", "Motion Graphics, 3D Graphics, Generative A.I., Interactive Art Installation, AR/MR/VR", "",
 H("Education", True), "",
 "Ph.D Student. Visual Communication Design, Hongik University, Seoul, KR",
 "MFA. Digital Arts, " + A(PRATT, "Pratt Institute") + ", New York, US",
 "BDes. Communication Design, " + A(SEOULTECH, "Seoul National University of Science and Technology") + ", Seoul, KR", "",
 H("Projects", True), "",
 "2026 National Museum of Modern and Contemporary Art Korea 40th Anniversary Motion Graphics Design",
 "2025 N" + A(NUPIP, "upip") + " Website Design Project Management",
] + plain([
 "2025 HYBE Weverse Magazine 'My K-pop Scrapbook' Design and Project Management",
 "2025 TCC Steel Website Renewal Design Project Management",
 "2024 Kia Autoland Gwangmyeong Experience Zone",
 "2022 《La Maschera del Tempo》at Il Teatro Verde, Venice, Italy",
 "2021 Kia Design Magazine",
 "2021 Arts Council Korea 《Invisible Cities》",
 "2021 Play 《Mobility》",
 "2021 Dazed Korea Aespa × GIVENCHY concept film",
 "2020 《Infection and Immunity》",
 "2020 KCDF 《Dialogue in Silence》",
 "2020 Shock Entertainment MR performance program",
 "2019 Arko Art Center Special Program 《Super Future Food》",
 "2019 Seoul National University of Science and Technology Exhibition Interactive Art",
 "2019 Shock Entertainment hologram projection lecture",
 "2019 Konkuk University Apparel Design Graduation Exhibition",
 "2019 《Festival Du Film De La Francophonie》",
 "2018 International Typography Biennale 《Typojanchi Saisai》",
 "2018 Pyeongchang Olympic Ceremony 《Song of Passion》",
 "2018 Donuimun Museum Village Seoul Regeneration Gallery",
 "2018 Rebel9 《Gyeonggi-do Memory, Library of Memory》",
 "2018 The War Memorial of Korea Interactive Media",
 "2018 Shock Entertainment Hologram Lecture",
 "2018 Wetax", "2018 2Ar Fashion Film", "2018 Meritz",
 "2017 International Typography Biennale 《Typojanchi》 Website",
 "2017 Rebel9 Interactive Art 《Typonotation》",
 "2017 National Gugak Center Interactive Art 《Gugak Interactive Archives Wall》",
 "2017 Gwacheon National Science Museum Interactive Media",
 "2017 Daegu National Science Museum Interactive Media",
 "2017 Grimdosi Commercial Film", "2017 Caseology Commercial Film", "2017 Doongle Commercial Film",
 "2017 Volkswagen Campaign Video", "2016 Movie 'Master'", "2015 PING F/W Fashion Film",
 "2015 G-Fair Korea Commercial Film", "2015 Linno Commercial Film", "2015 Haewoo Music Video", ""]) + [
 H("Exhibitions&amp;Film festival", True), ""] + plain([
 "2026 'Between Generation and Creation', Group Exhibition / Seoul, Korea",
 "2026 AMCA MBC C&I AI Film Festival / Seoul, Korea",
 "2025 Korea-China Art Exchange Exhibition / Dongguan, China",
 "2025 KOSMA Spring International Invitation Exhibition 'Light', Group Exhibition / Seoul, Korea",
 "2023 'DDA Art & Technology Exhibition', Group Exhibition / New York, USA",
 "2022 'Kickoff', Group Exhibition / New York, USA",
 "2022 'Untitled Art Fair', Group Exhibition / Miami, USA",
 "2021 'Gaea: A garden of the 2nd and 3rd Dimensions', Group Exhibition / New York, USA",
 "2021 'Hello, World!', Group Exhibition / New York, USA",
 "2021 'The Sky, The Earth, and The Real X', Solo Exhibition / Busan, Korea",
 "2020 'Infection and Immunity', Group Exhibition / Seoul, Korea",
 "2019 'BlindPoster', Group Exhibition / Seoul, Korea",
 "2018 'Young Creative Korea', Group Exhibition / Seoul, Korea",
 "2018 'OF', Three-Person Exhibition / Seoul, Korea",
 "2017 'BlindPoster', Group Exhibition / Seoul, Korea",
 "2017 'Seoul Design Week EP.age Youth Designer', Group Exhibition / Seoul, Korea",
 "2016 'Debut', Group Exhibition / Seoul, Korea", ""]) + [
 H("Lectures", True), ""] + plain([
 "2026 Lecture at Hongik University(Instructor)",
 "2026 Lecture at University of Suwon(Adjunct Professor)",
 "2025 Special Lecture at Seoul National University of Science and Technology",
 "2025 Special Lecture at Hongik University",
 "2024 Special Lecture at Seoul National University of Science and Technology", ""]) + [
 H("Activities", True), ""] + plain([
 "2025 Executive Manager of Exhibition Operations, KOS-MA",
 "2023 Artist Talk at Pratt Institute's Communication Design Department",
 "2022 Samsung Design Membership Emergence Project Exhibition 《Groovy Grove》 Tutor",
 "2021 Seoullo Media Canvas Exhibition 《Nature Project》 Examiner",
 "2019 Seoullo Media Canvas Exhibition Examiner",
 "2018 Open Talk Seminar Speaker",
 "2017 Seoul Design Week \"Design for a better relationship\" Youth Designer"])

HOME = {
 "ko": dict(
   h1="안녕하세요! 🙋🏻‍♂️<br>저는 디자이너 전성재입니다.",
   intro="저는 2017년 모션그래픽 디자이너로 경력을 시작한 이후 다양한 시각 디자인 및 미디어 분야에서 폭넓은 경험을 쌓았으며, 이탈리안 예술가 마티아 카살레뇨의 스튜디오와 뉴욕 첼시 지역의 아트 갤러리에서 근무하며 국제적인 감각을 익혔습니다. 현재는 서울에서 다각적인 클라이언트 프로젝트를 수행하며 경력을 이어가고 있습니다.",
   contact='<a href="mailto:jeonjayjeon@gmail.com">jeonjayjeon@gmail.com </a>'),
 "en": dict(
   h1="Hi!🙋‍♂️ I'm Jay Seongjae Jeon,<br>a multidisciplinary designer<br>based in Seoul and New York.",
   intro="I began my professional career at an interactive design company in 2017. While building my career, I became interested in exploring the intersection of design and art, and I achieved my master's in Digital Arts at Pratt Institute in New York.",
   contact='Feel free to reach out! 📮 <a href="mailto:jeonjayjeon@gmail.com">jeonjayjeon@gmail.com </a>'),
}

PAGES = {  # key: (en path, ko path, title)
 "home":  ("/", "/ko", "Jay Jeon 전성재 | 디자이너"),
 "cv":    ("/cv", "/ko/cv", "CV | Jay Jeon 전성재"),
 "album": ("/career-album", "/ko/career-album", "Career Album | Jay Jeon 전성재"),
}
DESC = "전성재는 시각 디자인과 경험 디자인의 교차점을 탐구하는 다학제적 디자이너입니다. | Jay Jeon 전성재"
CHEVRON = '<svg viewBox="0 0 12 6" aria-hidden="true"><path d="M.5.5 6 5.5 11.5.5" fill="none" stroke="currentColor"/></svg>'

def head(key, lang):
    en, ko, title = PAGES[key]
    url = SITE + (ko if lang == "ko" else en)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="x-default" href="{en}">
<link rel="alternate" hreflang="ko-kr" href="{ko}">
<link rel="alternate" hreflang="en-us" href="{en}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta property="og:image:width" content="750"><meta property="og:image:height" content="750">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Jay Jeon">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="naver-site-verification" content="b7ee066e6649f97f60b21cf32a4e8b878727b39a">
<meta name="google-site-verification" content="Fb9lCCuQ7e8otKbBvXD5j41bMVGgHaE_mvyssAUcnfk">
<link rel="icon" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400&display=swap">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body class="{lang}">
"""

def header(key, lang):
    en, ko, _ = PAGES[key]
    base = "/ko" if lang == "ko" else ""
    home = base or "/"
    other = ("EN", en, "en") if lang == "ko" else ("KO", ko, "ko")
    return f"""<header class="site-header"><div class="grid">
  <nav class="nav"><a class="n-home" href="{home}">Jay Jeon</a><a class="n-cv" href="{base}/cv">CV</a><a class="n-album" href="{base}/career-album">Career Album</a></nav>
  <div class="lang"><button class="lang-btn" type="button" aria-haspopup="listbox" aria-expanded="false" aria-label="Language Selector"><span class="cur">{lang.upper()}</span>{CHEVRON}</button>
    <ul class="lang-list" role="listbox"><li><a href="{other[1]}" data-lang="{other[2]}" hreflang="{other[2]}">{other[0]}</a></li></ul></div>
</div></header>
"""

FOOT = """<footer class="site-footer"><div class="grid"><p class="copyright">COPYRIGHT Jay Seongjae Jeon ⓒ 2026. ALL RIGHTS RESERVED.</p></div></footer>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""

def home(lang):
    h = HOME[lang]
    return head("home", lang) + header("home", lang) + f"""<main>
<section class="hero">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="auto" poster="/assets/video/hero-poster.jpg"><source src="/assets/video/hero.mp4" type="video/mp4"></video>
    <div class="overlay"></div>
  </div>
  <div class="grid">
    <h1>{h['h1']}</h1>
    <p class="intro">{h['intro']}</p>
    <p class="contact">{h['contact']}</p>
    <div class="social">
      <a href="https://www.linkedin.com/in/jeonjayjeon/" target="_blank" rel="noopener" aria-label="LinkedIn"><img src="/assets/icons/linkedin.png" alt="LinkedIn"></a>
      <a href="https://www.instagram.com/jeonjayjeon/" target="_blank" rel="noopener" aria-label="Instagram"><img src="/assets/icons/instagram.png" alt="Instagram"></a>
    </div>
  </div>
</section>
</main>
""" + FOOT

def cv(lang):
    lines = CV_KO if lang == "ko" else CV_EN
    body = "\n".join(f"<p>{l}</p>" if l else "<p>&#8203;</p>" for l in lines)
    return head("cv", lang) + header("cv", lang) + f"""<main>
<section class="cv"><div class="grid"><div class="text">
{body}
</div></div></section>
</main>
""" + FOOT

def album(lang):
    items = json.loads((ROOT / "album.json").read_text())
    out = []
    for it in items:
        f = it["f"].replace("~mv2", "")
        cap = html.escape(it[lang])
        out.append(f'<figure class="g-item" data-ratio="{it["h"]/590:.6f}" style="margin:0">'
                   f'<div class="g-img" style="aspect-ratio:590/{it["h"]}"><img src="/assets/img/album/{f}" alt="" loading="lazy"></div>'
                   f'<figcaption class="g-info">{cap}</figcaption></figure>')
    arrow = '<svg width="15" height="27" viewBox="0 0 15 27" aria-hidden="true"><path d="M1 1l12.5 12.5L1 26" fill="none" stroke="#fff" stroke-width="1.5"/></svg>'
    xsvg = '<svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M1 1l18 18M19 1 1 19" stroke="#fff" stroke-width="1.5"/></svg>'
    return head("album", lang) + header("album", lang) + f"""<main>
<section class="album"><div class="gallery">
{chr(10).join(out)}
</div></section>
</main>
<div class="lb" role="dialog" aria-modal="true">
  <div class="lb-stage"><img alt=""></div>
  <div class="lb-cap"></div>
  <button class="lb-btn lb-close" type="button" aria-label="Close">{xsvg}</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous">{arrow}</button>
  <button class="lb-btn lb-next" type="button" aria-label="Next">{arrow}</button>
</div>
""" + FOOT

def write(path, text):
    p = OUT / path.lstrip("/") / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)

for lang in ("en", "ko"):
    idx = 1 if lang == "ko" else 0
    write(PAGES["home"][idx], home(lang))
    write(PAGES["cv"][idx], cv(lang))
    write(PAGES["album"][idx], album(lang))

# asset list for download-assets.sh
items = json.loads((ROOT / "album.json").read_text())
with open(OUT / "assets.txt", "w") as fh:
    for it in items:
        fh.write(f"https://static.wixstatic.com/media/fb59a6_{it['f']} assets/img/album/{it['f'].replace('~mv2','')}\n")
print("built", OUT)
