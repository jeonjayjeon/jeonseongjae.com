# jeonseongjae.com: Wix 없이 만든 정적 사이트

## 폴더 구성
- site/: 실제로 배포하는 폴더입니다. 순수 HTML, CSS, JS로 되어 있고 빌드 과정이 필요 없습니다.
  - index.html, cv/, career-album/: 영문 페이지 (Wix와 같은 경로)
  - ko/, ko/cv/, ko/career-album/: 국문 페이지
  - assets/: CSS, JS, 이미지, 영상, 폰트
  - download-assets.sh: Wix에 올라가 있는 사진·영상·폰트를 assets로 내려받는 스크립트
- src/: 내용을 수정할 때 쓰는 원본 파일입니다.
  - album.json: Career Album 사진과 캡션 (국문/영문)
  - build.py: 메인·CV 텍스트와 페이지 템플릿. 실행하면 site/를 다시 생성합니다.

## 처음 한 번만 실행
```
cd site
bash download-assets.sh      # Wix 서버에서 사진 34장, 메인 영상, 아이콘, 폰트를 내려받음
python3 -m http.server 8000  # 내려받은 뒤 http://localhost:8000 에서 확인
```
주의: 페이지 경로가 /ko, /cv 같은 루트 기준이라 파일을 더블클릭해서 열면 깨집니다. 반드시 로컬 서버나 배포한 주소에서 확인하십시오.

## 내용 수정
src/album.json 또는 src/build.py의 텍스트를 고친 뒤 `python3 src/build.py`를 실행합니다.

## 배포
site 폴더를 Netlify, Cloudflare Pages, GitHub Pages, Vercel 중 한 곳에 올리고 jeonseongjae.com 도메인 DNS를 연결합니다.
Wix 연결을 해제하기 전에 download-assets.sh부터 실행하십시오. Wix를 해지하면 원본 파일 주소도 사라집니다.

## 원본과 동일하게 맞춘 항목 (1280px 화면 기준 실측값)
- 헤더와 푸터: sticky 고정, 메뉴 위치와 크기(17px, #d1d1d1), KO/EN 드롭다운, 저작권 문구(12px)
- 메인: 1275px 높이의 영상 배경, Wix 도트 오버레이 패턴(6×6 픽셀 단위로 재현), 제목·소개문·이메일·SNS 아이콘 위치
- 국문/영문 각각의 폰트: MinGothic, Maison Neue Extended, Noto Sans KR, Helvetica, SF UI Display
- CV: 섹션 제목 밑줄, 링크, 줄 간격
- Career Album: 2열 매소너리 배치(짧은 열부터 채움, 간격 20px, 캡션 영역 200px), 클릭하면 열리는 라이트박스(이전·다음·ESC)
- 브라우저 언어가 한국어면 /에서 /ko로 이동하는 동작. 드롭다운에서 언어를 고르면 그 선택을 기억합니다.
- 페이지 제목, 설명, OG 태그, hreflang, 네이버·구글 사이트 인증 메타 태그

## 원본과 다른 점
- 모바일: Wix의 별도 모바일 레이아웃은 재현하지 않았고, 1000px 미만에서는 반응형 레이아웃으로 바뀝니다.
- Helvetica: Wix가 라이선스를 갖고 제공하는 웹폰트 대신 기기에 설치된 Helvetica(맥/iOS) 또는 Arial을 씁니다.
- 라이트박스: Wix에서 사진마다 바뀌던 브라우저 탭 제목과 ?pgid 주소는 넣지 않았습니다.
- 폰트 라이선스: Maison Neue와 SF UI Display는 상용 또는 Apple 전용 폰트입니다. 자체 호스팅이 라이선스상 허용되는지 확인이 필요합니다.
