# 안산시 출장마사지 사이트 공통 설정

BASE_URL = "https://ansan-massage1.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시
NAV = [
    ("안산", "/", []),
    ("구별 안내", "/", [
        ("상록구", "/sangnok-gu/"),
        ("단원구", "/danwon-gu/"),
    ]),
    ("지역별 안내", "/", [
        ("중앙동", "/danwon-gu/jungang-dong/"),
        ("고잔동", "/danwon-gu/gojan-dong/"),
        ("초지동", "/danwon-gu/choji-dong/"),
        ("원곡동", "/danwon-gu/wongok-dong/"),
        ("선부동", "/danwon-gu/seonbu-dong/"),
        ("본오동", "/sangnok-gu/bono-dong/"),
        ("사동", "/sangnok-gu/sa-dong/"),
        ("월피동", "/sangnok-gu/wolpi-dong/"),
    ]),
    ("역세권 안내", "/", [
        ("상록수역", "/station/sangnoksu-station/"),
        ("한대앞역", "/station/hanyang-univ-at-ansan-station/"),
        ("중앙역", "/station/jungang-station/"),
        ("고잔역", "/station/gojan-station/"),
        ("초지역", "/station/choji-station/"),
        ("안산역", "/station/ansan-station/"),
        ("선부역", "/station/seonbu-station/"),
        ("원곡역", "/station/wongok-station/"),
        ("원시역", "/station/wonsi-station/"),
    ]),
    ("생활권 안내", "/", [
        ("중앙역·고잔", "/area/jungang-gojan/"),
        ("초지역·초지동", "/area/choji-dong/"),
        ("안산역·원곡동", "/area/ansan-station-wongok/"),
        ("상록수·본오", "/area/sangnoksu-bono/"),
        ("선부역·선부동", "/area/seonbu-station/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/check/", []),
    ("고객센터", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]

# ──────────────────────────────────────────
# 고객 평점·후기 (구조화 데이터 + 화면 표시 공용 데이터)
#
# ⚠ 중요: 아래 평점(RATING)과 후기(REVIEWS)는 대표 예시이며,
#   구글 정책상 실제 이용 고객의 후기로 교체·운영해야 합니다.
#   허위 평점/후기는 검색 스팸 정책 위반(수동 조치)의 대상이 될 수 있습니다.
#   화면에 보이는 후기 섹션과 schema.org Review 데이터는 항상 동일하게 유지하세요.
# ──────────────────────────────────────────
RATING = {"value": "4.9", "count": "138", "best": "5"}

REVIEWS = [
    {"author": "김○○", "rating": "5", "date": "2026-05-12",
     "body": "중앙역 근처 오피스텔로 예약했는데 시간 맞춰 방문해 주셔서 편했습니다. 예약 전 상담이 친절하고 안내가 정확했어요."},
    {"author": "이○○", "rating": "5", "date": "2026-04-28",
     "body": "고잔동 자택으로 방문 관리 받았습니다. 건물 출입 방식과 확인사항을 미리 꼼꼼히 안내해 줘서 믿을 수 있었어요."},
    {"author": "박○○", "rating": "5", "date": "2026-04-15",
     "body": "상록수역 인근에서 야간에 예약했는데 응대가 빠르고 위생 관리가 깔끔했습니다. 다음에도 이용할 생각입니다."},
    {"author": "최○○", "rating": "4", "date": "2026-03-30",
     "body": "초지역 근처에서 이용했어요. 추가 이동비 기준을 예약 전에 정확히 알려줘서 분쟁 없이 깔끔하게 마쳤습니다."},
    {"author": "정○○", "rating": "5", "date": "2026-03-18",
     "body": "사동 ERICA 근처 오피스텔이라 위치 설명이 어려웠는데 도착 전 연락 주셔서 헤매지 않았습니다. 만족합니다."},
]

# 사이트 전역 롱테일 내부링크 토픽 (모든 페이지 하단 '주제별 안내' 블록 공용)
TOPICS = [
    ("중앙역 오피스텔 출장마사지 예약", "/station/jungang-station/"),
    ("고잔동 호수공원 인근 홈타이 안내", "/danwon-gu/gojan-dong/"),
    ("초지역 트리플 역세권 출장마사지", "/station/choji-station/"),
    ("사동 ERICA 대학가 출장마사지", "/sangnok-gu/sa-dong/"),
    ("원곡동 다문화거리 홈타이 안내", "/danwon-gu/wongok-dong/"),
    ("상록수역 본오동 출장마사지", "/station/sangnoksu-station/"),
    ("선부역 서해선 출장마사지 안내", "/station/seonbu-station/"),
    ("대부도 펜션·숙소 출장마사지", "/danwon-gu/daebu-dong/"),
    ("안산역 원곡동 생활권 홈타이", "/area/ansan-station-wongok/"),
    ("분당선 한대앞역 대학가 안내", "/station/hanyang-univ-at-ansan-station/"),
    ("야간 예약 안심 출장마사지 안내", "/check/"),
    ("처음 이용자 출장마사지 예약 방법", "/reservation/"),
]
