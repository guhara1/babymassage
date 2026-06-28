# 수도권 사이트 공용 콘텐츠 헬퍼
#
# 모든 콘텐츠 모듈(main, safe_booking, report, use_cases, policy,
# seoul, gyeonggi, incheon, stations)이 이 헬퍼를 사용해 페이지를 구성한다.
# - 고유 본문(지역 특성/리포트/설명)은 각 모듈이 직접 작성한다.
# - 반복되는 신뢰 블록(안심 예약 기준 요약·문의 전 체크리스트·FAQ·관련 링크)은
#   여기 빌더로 생성해 일관성을 유지하되, region 인자로 맥락을 다르게 둔다.
#
# 주의(지시서 §18): 가격 강조 페이지·과장 표현 금지. 요금 블록은 두지 않는다.


def create_page(path, title, desc, h1, breadcrumb, body, noindex=False):
    """페이지 dict 생성. noindex=True 면 본문 길이와 무관하게 색인 제외."""
    page = {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body,
    }
    if noindex:
        page["noindex"] = True
    return page


def section(h2, *paragraphs, sid=None):
    """<section><h2>..</h2><p>..</p>..</section> 한 블록."""
    idattr = f' id="{sid}"' if sid else ""
    inner = "".join(
        p if p.strip().startswith("<") else f"<p>{p}</p>" for p in paragraphs
    )
    return f"<section{idattr}><h2>{h2}</h2>{inner}</section>"


def ul(items):
    """<ul><li>..</li></ul>. items 는 문자열 리스트(HTML 허용)."""
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def links_ul(pairs):
    """(label, href) 리스트 → 내부링크 <ul>. 롱테일 앵커 권장."""
    return "<ul>" + "".join(
        f'<li><a href="{href}">{label}</a></li>' for label, href in pairs
    ) + "</ul>"


def faq_section(items, h2="자주 묻는 질문(FAQ)"):
    """(질문, 답변) 리스트 → FAQPage 대응 가시 FAQ 섹션.
    build.py 는 FAQ dl 을 별도 FAQPage 스키마로 자동 변환하지 않으므로,
    FAQPage 스키마가 필요한 페이지는 extra_head 로 직접 넣는다(메인 등)."""
    rows = "".join(f"<dt>{q}</dt><dd>{a}</dd>" for q, a in items)
    return f'<section><h2>{h2}</h2><dl class="faq-list">{rows}</dl></section>'


def safe_booking_summary(region="수도권"):
    """예약 전 신뢰 기준 요약 + 안심 예약 기준 메뉴로의 내부링크."""
    body = (
        f"<p>{region} 방문형 서비스는 지역마다 이동 기준과 건물 출입 방식이 달라, "
        "예약 전 아래 기준을 먼저 확인하면 방문 과정이 한결 수월합니다. "
        "모든 일정은 건전한 방문 관리 서비스 기준 안에서만 진행되며, "
        "불법·선정적 요청에는 어떤 경우에도 응하지 않습니다.</p>"
    )
    body += links_ul([
        ("처음 이용 전 확인할 내용", "/safe-booking/first-time/"),
        ("개인정보 처리 기준", "/safe-booking/privacy-standard/"),
        ("불법·선정 서비스 불가 안내", "/safe-booking/service-policy/"),
        ("추가 이동비 기준", "/safe-booking/travel-fee/"),
        ("건물 출입 방식", "/safe-booking/building-access/"),
        ("예약 변경 기준", "/safe-booking/reschedule/"),
    ])
    return f"<section><h2>{region} 안심 예약 기준</h2>{body}</section>"


def checklist_section():
    """문의 전 체크리스트 (지시서 §16 Section 5)."""
    items = [
        "방문 주소를 정확히 확인했나요? (단지명·동·호수 또는 건물명·호실)",
        "공동현관 또는 건물 출입 방식이 있나요?",
        "호텔·숙소 이용 가능 여부를 확인했나요?",
        "오피스텔 관리 규정이 있나요?",
        "주차 또는 차량 이동이 필요한 지역인가요?",
        "외곽 지역 추가 이동비가 있는지 확인했나요?",
        "공항·도서 지역 사전 예약이 필요한가요?",
        "예약 변경 기준을 확인했나요?",
        "개인정보 처리 기준을 확인했나요?",
        '<a href="/safe-booking/service-policy/">불법·선정적 서비스 불가 안내</a>를 확인했나요?',
    ]
    return f"<section><h2>문의 전 확인하면 좋은 내용</h2>{ul(items)}</section>"


def related_section(pairs, h2="관련 안내 보기"):
    """관련 페이지 내부링크 섹션 (롱테일 앵커)."""
    return f"<section><h2>{h2}</h2>{links_ul(pairs)}</section>"
