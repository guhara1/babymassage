import json
from .site import BRAND, BASE_URL

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "서울·경기·인천 출장마사지·홈타이 예약 전 방문 지역, 이용 장소, 개인정보 기준, 추가 이동비를 안내합니다."

# 자주 묻는 질문 (FAQ 스키마 + 화면 공용)
_FAQ = [
    ("수도권 출장마사지는 어떤 서비스인가요?",
     "고객의 자택·숙소·오피스텔 등으로 전문가가 방문하여 관리하는 방문형 서비스입니다. 서울·경기·인천 주요 생활권으로 방문 가능하며, 예약 전 방문 가능 지역과 기준을 먼저 확인하시면 좋습니다."),
    ("서울·경기·인천은 예약 기준이 다른가요?",
     "네. 서울은 지하철역과 생활권이 촘촘하고, 경기는 시군 범위가 넓어 차량 이동 기준이 중요하며, 인천은 원도심·신도시·공항·도서 지역이 함께 있어 사전 확인이 필요합니다. 그래서 지역명보다 안심 예약 기준을 먼저 안내합니다."),
    ("예약 전 꼭 확인해야 할 사항은?",
     "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 개인정보 처리 기준을 먼저 확인하고 예약하는 방식이 좋습니다. 예약 전 체크리스트에서 항목을 정리해 두었습니다."),
    ("추가 이동비는 어떻게 계산되나요?",
     "서울 도심, 경기 외곽, 인천 공항·도서 지역은 이동 기준이 달라 추가 이동비가 발생할 수 있습니다. 실제 비용은 예약 시 사전에 확인하는 것을 원칙으로 합니다."),
    ("불법·선정적 서비스도 가능한가요?",
     "아니요. 간다GO는 건전한 방문 관리 서비스만 운영하며, 불법·선정적 요청에는 어떤 경우에도 응하지 않습니다."),
]

_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "@id": f"#faq-{i+1}", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for i, (q, a) in enumerate(_FAQ)
    ],
}

_webpage_schema = {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "서울·경기·인천 출장마사지｜수도권 안심 예약·홈타이 지역 안내",
    "description": DESC,
    "url": _BASE + "/",
    "inLanguage": "ko",
    "isPartOf": {"@id": _BASE + "/#organization"},
    "publisher": {"@id": _BASE + "/#organization"},
    "primaryImageOfPage": {"@id": _BASE + "/#primaryimage"},
}

_image_schema = {
    "@context": "https://schema.org",
    "@type": "ImageObject",
    "@id": _BASE + "/#primaryimage",
    "url": _BASE + "/assets/og-image.png",
    "contentUrl": _BASE + "/assets/og-image.png",
    "width": 1200,
    "height": 630,
    "caption": "서울·경기·인천 출장마사지·홈타이 지역 안내 — " + BRAND,
}

_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "홈", "item": _BASE + "/"}
    ],
}

_EXTRA_HEAD = "".join(
    '<script type="application/ld+json">\n' + json.dumps(s, ensure_ascii=False, indent=2) + "\n</script>\n"
    for s in (_webpage_schema, _image_schema, _breadcrumb_schema, _faq_schema)
)

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">서울·경기·인천 수도권 방문 관리</div>
    <h1 class="hero-title">서울·경기·인천 출장마사지<br><span class="hero-accent">수도권 안심 예약 안내</span></h1>
    <p class="hero-lead">서울, 경기, 인천 주요 생활권별 방문 가능 지역과 개인정보 기준, 불법·선정적 서비스 불가 안내, 추가 이동비, 이용 장소별 확인사항을 안내합니다.</p>
    <div class="hero-cta">
      <a href="/safe-booking/" class="btn btn-primary">안심 예약 기준</a>
      <a href="/report/" class="btn btn-secondary">지역 리포트</a>
      <a href="/seoul/" class="btn btn-secondary">서울 보기</a>
      <a href="/gyeonggi/" class="btn btn-secondary">경기 보기</a>
      <a href="/incheon/" class="btn btn-secondary">인천 보기</a>
      <a href="/contact/" class="btn btn-secondary">문의하기</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-number">3</div><div class="stat-label">시·도 권역</div></div>
    <div class="stat"><div class="stat-number">66+</div><div class="stat-label">시군구 안내</div></div>
    <div class="stat"><div class="stat-number">28</div><div class="stat-label">대표 생활권</div></div>
    <div class="stat"><div class="stat-number">24H</div><div class="stat-label">상담 가능</div></div>
  </div>
</div>"""

PAGE = {
    "path": "",
    "title": "서울·경기·인천 출장마사지｜수도권 안심 예약·홈타이 지역 안내",
    "desc": DESC,
    "h1": "서울·경기·인천 출장마사지 · 수도권 안심 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="intro">
  <h2>수도권 방문형 서비스는 예약 전 기준 확인이 중요합니다</h2>
  <p>서울, 경기, 인천은 같은 수도권이라도 지역 구조와 이동 기준이 크게 다릅니다. 서울은 지하철역과 생활권이 촘촘하게 연결되어 있어 역세권과 생활권 중심으로 방문 지역을 확인하는 것이 편리하고, 경기는 시군의 면적이 넓어 같은 시 안에서도 차량 이동 기준이 달라집니다. 인천은 원도심, 신도시, 공항, 도서 지역이 함께 있어 권역별로 사전 확인이 필요합니다.</p>
  <p>그래서 간다GO는 지역명을 먼저 나열하기보다, 예약 전 확인해야 할 안심 예약 기준과 지역 리포트를 먼저 안내합니다. 아래 순서대로 안심 예약 기준 → 지역 리포트 → 시·도별 안내 → 이용 장소별 기준을 확인하시면 수도권 어디서든 방문 일정을 정확히 잡을 수 있습니다. 모든 서비스는 건전한 방문 관리 기준 안에서만 제공되며, 불법·선정적 요청에는 응하지 않습니다.</p>
</section>

<section id="safe-booking">
  <h2>예약 전 확인해야 할 안심 예약 기준</h2>
  <p>지역 페이지보다 먼저, 방문형 서비스 이용 시 확인해야 할 기준을 정리했습니다.</p>
  <div class="card-grid">
    <a href="/safe-booking/first-time/" class="card"><h3>처음 이용하는 분</h3><p>방문 주소·시간·이동비 등 처음 확인할 내용</p><span class="card-arrow">→</span></a>
    <a href="/safe-booking/privacy-standard/" class="card"><h3>개인정보 처리 기준</h3><p>예약에 필요한 최소 정보만 받는 기준</p><span class="card-arrow">→</span></a>
    <a href="/safe-booking/service-policy/" class="card"><h3>불법·선정 서비스 불가</h3><p>건전한 방문 관리 서비스 운영 기준</p><span class="card-arrow">→</span></a>
    <a href="/safe-booking/travel-fee/" class="card"><h3>추가 이동비 기준</h3><p>도심·외곽·공항·도서 이동 기준 안내</p><span class="card-arrow">→</span></a>
    <a href="/safe-booking/building-access/" class="card"><h3>건물 출입 방식</h3><p>공동현관·오피스텔·숙소 출입 확인</p><span class="card-arrow">→</span></a>
    <a href="/safe-booking/reschedule/" class="card"><h3>예약 변경 기준</h3><p>예약 변경·취소 절차 안내</p><span class="card-arrow">→</span></a>
  </div>
</section>

<section id="report">
  <h2>서울·경기·인천 지역 리포트</h2>
  <p>지역을 단순히 나열하지 않고, 권역 특성별로 방문 기준과 생활권을 정리했습니다.</p>
  <div class="card-grid">
    <a href="/report/seoul/" class="card"><h3>서울 리포트</h3><p>역세권·생활권 중심의 도심 권역</p></a>
    <a href="/report/gyeonggi/" class="card"><h3>경기 리포트</h3><p>넓은 시군·차량 이동 중심 권역</p></a>
    <a href="/report/incheon/" class="card"><h3>인천 리포트</h3><p>원도심·신도시·공항·도서 혼합 권역</p></a>
    <a href="/report/downtown/" class="card"><h3>도심형 리포트</h3><p>상권·관광·업무 밀집 도심 권역</p></a>
    <a href="/report/newtown/" class="card"><h3>신도시형 리포트</h3><p>아파트 대단지·오피스텔 신도시</p></a>
    <a href="/report/business/" class="card"><h3>업무지구형 리포트</h3><p>오피스·빌딩 밀집 업무 권역</p></a>
    <a href="/report/airport-island/" class="card"><h3>공항·도서형 리포트</h3><p>공항권·섬 지역 사전 예약 권역</p></a>
    <a href="/report/outer/" class="card"><h3>외곽 이동형 리포트</h3><p>차량 이동·추가 이동비 권역</p></a>
  </div>
</section>

<section id="life">
  <h2>수도권 주요 생활권 안내</h2>
  <p>서울·경기·인천의 대표 생활권별로 방문 가능 지역과 가까운 역을 확인할 수 있습니다.</p>
  <div class="linkhub">
    <div class="linkhub-col">
      <h3>서울 대표 생활권</h3>
      <ul>
        <li><a href="/seoul/life/gangnam-yeoksam/">강남역·역삼 출장마사지 생활권</a></li>
        <li><a href="/seoul/life/jamsil-songpa/">잠실·송파 홈타이 생활권</a></li>
        <li><a href="/seoul/life/hongdae-hapjeong/">홍대·합정 출장마사지 생활권</a></li>
        <li><a href="/seoul/life/yeouido-yeongdeungpo/">여의도·영등포 업무권 안내</a></li>
        <li><a href="/seoul/life/seongsu-wangsimni/">성수·왕십리 생활권 안내</a></li>
        <li><a href="/seoul/life/yongsan-seoul-station/">용산·서울역 숙소 인접권</a></li>
      </ul>
    </div>
    <div class="linkhub-col">
      <h3>경기 대표 생활권</h3>
      <ul>
        <li><a href="/gyeonggi/life/suwon-station-ingye/">수원역·인계동 출장마사지 생활권</a></li>
        <li><a href="/gyeonggi/life/bundang-pangyo/">분당·판교 신도시 홈타이</a></li>
        <li><a href="/gyeonggi/life/dongtan-newtown/">동탄신도시 출장마사지 안내</a></li>
        <li><a href="/gyeonggi/life/bucheon-station-sangdong/">부천역·상동 역세권 안내</a></li>
        <li><a href="/gyeonggi/life/ilsan-kintex/">일산·킨텍스 생활권 안내</a></li>
        <li><a href="/gyeonggi/life/hanam-misa/">하남·미사 신도시 홈타이</a></li>
      </ul>
    </div>
    <div class="linkhub-col">
      <h3>인천 대표 생활권</h3>
      <ul>
        <li><a href="/incheon/life/songdo-international-city/">송도국제도시 출장마사지 안내</a></li>
        <li><a href="/incheon/life/guwol-incheon-cityhall/">구월·인천시청 생활권 안내</a></li>
        <li><a href="/incheon/life/bupyeong-station-market/">부평역·부평시장 역세권</a></li>
        <li><a href="/incheon/life/cheongna-international-city/">청라국제도시 홈타이 안내</a></li>
        <li><a href="/incheon/life/yeongjong-unseo/">영종·운서 공항권 안내</a></li>
        <li><a href="/incheon/life/incheon-airport/">인천공항 인근 숙소 안내</a></li>
      </ul>
    </div>
    <div class="linkhub-col">
      <h3>이용 장소별 안내</h3>
      <ul>
        <li><a href="/use/home/">자택 이용 출장마사지 기준</a></li>
        <li><a href="/use/hotel/">호텔·숙소 이용 홈타이 안내</a></li>
        <li><a href="/use/officetel/">오피스텔 이용 출장마사지</a></li>
        <li><a href="/use/business-district/">업무지구 이용 안내</a></li>
        <li><a href="/use/night/">야간 예약 안심 안내</a></li>
        <li><a href="/use/outer-area/">외곽 지역 이용 안내</a></li>
      </ul>
    </div>
  </div>
</section>

<section id="checklist">
  <h2>문의 전 확인하면 좋은 내용</h2>
  <p>예약·문의 전에 아래 항목을 먼저 확인하면 방문 일정이 훨씬 정확해집니다.</p>
  <ul>
    <li>방문 주소를 정확히 확인했나요? (단지명·동·호수 또는 건물명·호실)</li>
    <li>공동현관 또는 건물 출입 방식이 있나요?</li>
    <li>호텔·숙소 이용 가능 여부를 확인했나요?</li>
    <li>오피스텔 관리 규정이 있나요?</li>
    <li>주차 또는 차량 이동이 필요한 지역인가요?</li>
    <li>외곽 지역 추가 이동비가 있는지 확인했나요?</li>
    <li>공항·도서 지역 사전 예약이 필요한가요?</li>
    <li>예약 변경 기준을 확인했나요?</li>
    <li>개인정보 처리 기준을 확인했나요?</li>
    <li><a href="/safe-booking/service-policy/">불법·선정적 서비스 불가 안내</a>를 확인했나요?</li>
  </ul>
</section>

<section id="faq">
  <h2>수도권 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
""" + "".join(f"    <dt id=\"faq-{i+1}\">{q}</dt>\n    <dd>{a}</dd>\n" for i, (q, a) in enumerate(_FAQ)) + """  </dl>
</section>
""",
}
