# 수도권(서울·경기·인천) 출장마사지 — 공통 설정

# ⚠ 배포 도메인 확정 시 BASE_URL 을 실제 주소로 교체하세요.
BASE_URL = "https://sudogwon-massage.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 서비스 권역 (스키마 areaServed)
AREA_SERVED = "서울·경기·인천 수도권"

# 상단 메뉴 — 키워드 반복 없이 지역명·기준명만 표시 (지시서 §4)
NAV = [
    ("수도권 홈", "/", []),
    ("안심 예약 기준", "/safe-booking/", [
        ("처음 이용하는 분", "/safe-booking/first-time/"),
        ("예약 전 체크리스트", "/safe-booking/checklist/"),
        ("개인정보 처리 기준", "/safe-booking/privacy-standard/"),
        ("불법·선정 서비스 불가", "/safe-booking/service-policy/"),
        ("추가 이동비 기준", "/safe-booking/travel-fee/"),
        ("건물 출입 방식", "/safe-booking/building-access/"),
        ("예약 변경 기준", "/safe-booking/reschedule/"),
        ("고객 유의사항", "/safe-booking/customer-notice/"),
    ]),
    ("지역 리포트", "/report/", [
        ("서울 리포트", "/report/seoul/"),
        ("경기 리포트", "/report/gyeonggi/"),
        ("인천 리포트", "/report/incheon/"),
        ("도심형", "/report/downtown/"),
        ("신도시형", "/report/newtown/"),
        ("업무지구형", "/report/business/"),
        ("주거형", "/report/residential/"),
        ("공항·도서형", "/report/airport-island/"),
        ("외곽 이동형", "/report/outer/"),
    ]),
    ("서울", "/seoul/", [
        ("서울 홈", "/seoul/"),
        ("업무지구", "/seoul/group/business/"),
        ("숙소 인접권", "/seoul/group/hotel-area/"),
        ("주거 생활권", "/seoul/group/residential/"),
        ("도심·관광권", "/seoul/group/downtown/"),
    ]),
    ("경기", "/gyeonggi/", [
        ("경기 홈", "/gyeonggi/"),
        ("남부 핵심권", "/gyeonggi/group/south-core/"),
        ("북부 생활권", "/gyeonggi/group/north-life/"),
        ("서부 역세권", "/gyeonggi/group/west-station/"),
        ("동부·신도시권", "/gyeonggi/group/east-newtown/"),
        ("외곽 이동권", "/gyeonggi/group/outer-mobility/"),
    ]),
    ("인천", "/incheon/", [
        ("인천 홈", "/incheon/"),
        ("신도시권", "/incheon/group/newtown/"),
        ("원도심권", "/incheon/group/old-town/"),
        ("공항권", "/incheon/group/airport/"),
        ("도서권", "/incheon/group/islands/"),
    ]),
    ("이용 장소", "/use/", [
        ("자택 이용", "/use/home/"),
        ("호텔·숙소 이용", "/use/hotel/"),
        ("오피스텔 이용", "/use/officetel/"),
        ("업무지구 이용", "/use/business-district/"),
        ("역세권 이용", "/use/station-area/"),
        ("야간 예약", "/use/night/"),
        ("외곽 지역 이용", "/use/outer-area/"),
    ]),
    ("문의하기", "/contact/", []),
]

# ──────────────────────────────────────────
# 고객 평점·후기 (구조화 데이터 + 화면 표시 공용 데이터)
#
# ⚠ 중요: 아래 평점(RATING)과 후기(REVIEWS)는 대표 예시이며,
#   구글 정책상 실제 이용 고객의 후기로 교체·운영해야 합니다.
#   허위 평점/후기는 검색 스팸 정책 위반(수동 조치)의 대상이 될 수 있습니다.
#   화면에 보이는 후기 섹션과 schema.org Review 데이터는 항상 동일하게 유지하세요.
# ──────────────────────────────────────────
RATING = {"value": "4.9", "count": "212", "best": "5"}

REVIEWS = [
    {"author": "김○○", "rating": "5", "date": "2026-05-20",
     "body": "강남 업무지구 오피스텔로 예약했는데 시간 맞춰 방문해 주셔서 편했습니다. 예약 전 상담이 친절하고 안내가 정확했어요."},
    {"author": "이○○", "rating": "5", "date": "2026-05-06",
     "body": "분당 자택으로 방문 관리 받았습니다. 건물 출입 방식과 확인사항을 미리 꼼꼼히 안내해 줘서 믿을 수 있었어요."},
    {"author": "박○○", "rating": "5", "date": "2026-04-22",
     "body": "인천 송도 숙소로 야간에 예약했는데 응대가 빠르고 위생 관리가 깔끔했습니다. 다음에도 이용할 생각입니다."},
    {"author": "최○○", "rating": "4", "date": "2026-04-09",
     "body": "수원역 인근에서 이용했어요. 추가 이동비 기준을 예약 전에 정확히 알려줘서 분쟁 없이 깔끔하게 마쳤습니다."},
    {"author": "정○○", "rating": "5", "date": "2026-03-25",
     "body": "부천 상동 오피스텔이라 위치 설명이 어려웠는데 도착 전 연락 주셔서 헤매지 않았습니다. 만족합니다."},
]

# 사이트 전역 롱테일 내부링크 토픽 (모든 페이지 하단 '주제별 안내' 블록 공용)
TOPICS = [
    ("강남 업무지구 출장마사지 예약 안내", "/seoul/group/business/"),
    ("분당·판교 신도시 홈타이 생활권", "/gyeonggi/life/bundang-pangyo/"),
    ("송도국제도시 출장마사지 안내", "/incheon/life/songdo-international-city/"),
    ("수원역·인계동 출장마사지 생활권", "/gyeonggi/life/suwon-station-ingye/"),
    ("서울 숙소 인접권 호텔 홈타이", "/seoul/group/hotel-area/"),
    ("부천역·상동 출장마사지 역세권", "/gyeonggi/life/bucheon-station-sangdong/"),
    ("인천 공항권 영종·운서 안내", "/incheon/group/airport/"),
    ("오피스텔 이용 출장마사지 기준", "/use/officetel/"),
    ("야간 예약 안심 홈타이 안내", "/use/night/"),
    ("처음 이용자 출장마사지 예약 방법", "/safe-booking/first-time/"),
    ("추가 이동비 기준 사전 확인 안내", "/safe-booking/travel-fee/"),
    ("불법·선정 서비스 불가 안내", "/safe-booking/service-policy/"),
]
