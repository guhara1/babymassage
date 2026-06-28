# 안산 정보 페이지 — 5개 (예약, 가이드, 정책 등)

def create_info_page(path, title, desc, h1, breadcrumb, body_content):
    """정보 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 5개 정보 페이지 =====

reservation = create_info_page(
    path="reservation/",
    title="예약 안내｜안산 출장마사지·홈타이 예약 방법",
    desc="안산 출장마사지·홈타이 예약 방법, 취소 정책, 서비스 시간을 확인하세요.",
    h1="예약 안내",
    breadcrumb=[("안산", "/"), ("예약 안내", "")],
    body_content="""
<section>
<h2>안산 출장마사지 예약 방법</h2>
<p>간다GO의 <a href="/">안산 출장마사지</a>·홈타이 예약은 전화 한 통으로 간단하게 진행됩니다. 별도의 앱 설치나 회원가입 없이, 상담원과 통화하면서 방문 지역과 희망 시간, 서비스 시간을 정한 뒤 그 자리에서 예약이 확정됩니다. 처음 이용하시는 분도 부담 없이 문의하실 수 있도록 24시간 상담 창구를 운영합니다.</p>
<ul>
<li><strong>전화 예약</strong>: <a href="tel:0508-202-4719">0508-202-4719</a> (연중무휴 24시간 상담)</li>
<li><strong>상담 시간</strong>: 야간·새벽을 포함한 24시간 응대</li>
<li><strong>예약 확인</strong>: 통화 중 방문 시간과 위치를 함께 확인</li>
<li><strong>방문 일정</strong>: 상담 후 가능한 시간대로 협의하여 결정</li>
</ul>
<p>예약 전에 <a href="/check/">이용 전 확인사항</a>을 미리 읽어 두시면, 방문 당일 건물 출입과 결제 과정이 한결 매끄럽게 진행됩니다.</p>
</section>

<section>
<h2>예약 시 필요한 정보</h2>
<p>원활한 방문 일정을 잡기 위해 예약 전화 시 아래 정보를 정확히 알려주시면 좋습니다. 정보가 정확할수록 방문 시간이 지체되지 않고, 길을 잃거나 건물을 찾지 못해 생기는 불편을 줄일 수 있습니다.</p>
<ol>
<li><strong>방문 지역</strong>: 구·동 또는 인근 역명 (예: <a href="/sangnok-gu/">상록구 출장마사지 안내</a>, <a href="/station/jungang-station/">중앙역</a> 인근)</li>
<li><strong>정확한 주소</strong>
  <ul>
  <li>아파트 단지: 단지명, 동·호수, 공동현관 비밀번호 또는 호출 방법</li>
  <li>주택·오피스텔: 도로명 주소와 건물명, 층·호수</li>
  <li>숙소·상업 시설: 건물명 또는 상호, 객실 번호</li>
  </ul>
</li>
<li><strong>희망 방문 시간</strong>: 원하는 시간대 (야간·새벽 포함)</li>
<li><strong>이용 시간</strong>: 1시간·2시간·3시간 등 원하는 서비스 길이</li>
<li><strong>연락처</strong>: 통화 및 도착 안내가 가능한 휴대폰 번호</li>
</ol>
</section>

<section>
<h2>서비스 요금 안내</h2>
<p>간다GO의 안산 출장마사지·홈타이 요금은 서비스 시간에 따라 결정됩니다:</p>
<ul>
<li><strong>1시간</strong>: 70,000원~</li>
<li><strong>2시간</strong>: 140,000원~</li>
<li><strong>3시간</strong>: 210,000원~</li>
</ul>
<p>정확한 가격은 지역, 시간대, 서비스 내용에 따라 상이할 수 있습니다. <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>

<section>
<h2>예약 변경 및 취소 기준</h2>
<p>갑작스러운 일정 변동이 생기면 가급적 빠르게 연락 주시기 바랍니다. 미리 알려주실수록 방문 일정 조율이 수월하고, 다른 고객의 예약 시간과도 겹치지 않게 조정할 수 있습니다. 아래 기준은 일반적인 안내이며, 구체적인 적용은 예약 시 상담 내용에 따릅니다.</p>
<ul>
<li><strong>예약 변경</strong>: 방문 예정 시간 전 연락 시 가능한 시간대로 재조정</li>
<li><strong>예약 24시간 전 취소</strong>: 전액 환불</li>
<li><strong>예약 12시간 전 취소</strong>: 50% 환불</li>
<li><strong>예약 1시간 전·당일 취소</strong>: 환불이 어려울 수 있음</li>
<li><strong>무단 불출현</strong>: 환불 불가</li>
</ul>
<p>정확한 취소·환불 기준은 예약 확정 시 상담 내용을 기준으로 적용됩니다.</p>
</section>

<section>
<h2>서비스 시간 및 방문 가능 지역</h2>
<p>간다GO는 안산시 전 지역을 대상으로 야간과 새벽을 포함한 시간대에 방문 일정을 잡을 수 있습니다. 자택은 물론 오피스텔, 숙소 등 고객이 머무는 공간으로 방문하는 형태이므로, 방문지 주소만 정확하면 지역에 큰 제약 없이 일정 조율이 가능합니다.</p>
<ul>
<li><strong>상록구</strong>: <a href="/sangnok-gu/">상록구 출장마사지 안내</a> — 사동, 본오동, 이동 등</li>
<li><strong>단원구</strong>: <a href="/danwon-gu/">단원구 출장마사지 안내</a> — 고잔동, 중앙동, 초지동 등</li>
<li><strong>주요 역 인근</strong>: <a href="/station/gojan-station/">고잔역</a>, <a href="/station/jungang-station/">중앙역</a>, <a href="/station/sangnoksu-station/">상록수역</a> 주변</li>
</ul>
<p>방문지가 위 목록에 없더라도 안산시 내라면 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의해 주시면 방문 가능 여부를 안내해 드립니다.</p>
</section>

<section>
<h2>접근성 안내</h2>
<p>서비스를 위해 다음 사항을 미리 알려주세요:</p>
<ul>
<li><strong>아파트 단지</strong>: 외부인 출입 가능 여부, 보안 게이트 여부</li>
<li><strong>엘리베이터</strong>: 위치 및 사용 가능 여부</li>
<li><strong>주차</strong>: 단지 내 주차 가능 여부, 주차 위치</li>
<li><strong>접근로</strong>: 계단 또는 엘리베이터 위치</li>
<li><strong>야간 출입</strong>: 야간 시간의 특별 출입 방법</li>
</ul>
</section>

<section>
<h2>결제 방법</h2>
<p>결제는 <strong>서비스 후 현장에서</strong> 진행됩니다:</p>
<ul>
<li><strong>현금 결제</strong>: 서비스 완료 후 현금 지급</li>
<li><strong>카드 결제</strong>: 현장 카드 결제 가능 (문의)</li>
<li><strong>계좌이체</strong>: 미리 계약 시 가능</li>
</ul>
</section>

<section>
<h2>안전 및 신뢰</h2>
<p>간다GO는 <a href="/check/">이용 전 확인사항</a>을 꼭 읽으신 후 예약하시기를 권장합니다. 건전하고 안전한 서비스 이용을 위해 필요한 모든 정보를 담고 있습니다.</p>
</section>

<section>
<h2>예약 자주 묻는 질문</h2>
<dl class="faq-list">
<dt>예약 직후 바로 방문이 가능한가요?</dt>
<dd>상담 시점의 일정에 여유가 있다면 빠른 방문도 가능합니다. 다만 시간대와 지역에 따라 대기가 생길 수 있으므로, 정확한 방문 가능 시각은 <a href="tel:0508-202-4719">0508-202-4719</a> 전화 상담에서 확인해 주세요.</dd>
<dt>야간이나 새벽에도 예약할 수 있나요?</dt>
<dd>네. 간다GO는 연중무휴 24시간 상담을 운영하므로 야간·새벽 시간대 방문 일정도 조율할 수 있습니다.</dd>
<dt>정기적으로 같은 시간에 예약할 수 있나요?</dt>
<dd>가능합니다. 원하시는 요일과 시간대를 상담 시 말씀해 주시면 정기 방문 일정으로 조율해 드립니다.</dd>
<dt>예약한 주소를 당일에 변경해도 되나요?</dt>
<dd>방문 전이라면 변경 가능합니다. 다만 지역이 크게 달라지면 이동 시간이 필요하므로, 변경 사실을 확인되는 즉시 알려주시기 바랍니다.</dd>
<dt>예약 전에 무엇을 먼저 확인하면 좋을까요?</dt>
<dd>방문지 주소와 건물 출입 방법을 미리 정리해 두시면 좋습니다. 자세한 내용은 <a href="/check/">이용 전 확인사항</a>에서 안내하고 있습니다.</dd>
</dl>
</section>

<section>
<h2>예약 연락처</h2>
<p><strong>간다GO</strong></p>
<ul>
<li><strong>예약 전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a></li>
<li><strong>상담 시간</strong>: 연중무휴 24시간</li>
<li><strong>서비스 지역</strong>: 안산시 전지역</li>
</ul>
</section>
"""
)

check = create_info_page(
    path="check/",
    title="이용 전 확인사항｜안산 출장마사지·홈타이 안전 가이드",
    desc="출장마사지·홈타이 이용 전 반드시 확인해야 할 안전 사항을 안내합니다.",
    h1="이용 전 확인사항",
    breadcrumb=[("안산", "/"), ("이용 전 확인사항", "")],
    body_content="""
<section>
<h2>간다GO 이용 전 안내</h2>
<p><strong>간다GO</strong>는 안산시에서 건전하고 안전한 출장마사지·홈타이 방문 관리 서비스를 제공합니다. 불법적이거나 선정적인 요청에는 어떤 경우에도 응하지 않으며, 고객과 관리사 모두의 안전과 신뢰를 최우선으로 합니다. 이 페이지는 방문 전 알아두면 좋은 사항을 모아 둔 것으로, <a href="/reservation/">안산 출장마사지 예약 안내</a>와 함께 읽으시면 방문 당일 진행이 훨씬 매끄럽습니다.</p>
</section>

<section>
<h2>방문 주소 및 건물 출입 확인</h2>
<p>방문형 서비스에서 가장 중요한 것은 정확한 주소와 출입 방법입니다. 아래 사항을 예약 시 미리 정리해 두시면, 관리사가 건물을 찾지 못해 시간이 지체되는 일을 막을 수 있습니다.</p>
<ul>
<li><strong>도로명 주소</strong>: 동·호수까지 정확히 (지번만으로는 건물 특정이 어려울 수 있음)</li>
<li><strong>공동현관</strong>: 아파트·오피스텔의 공동현관 비밀번호 또는 세대 호출 방법</li>
<li><strong>관리실 안내</strong>: 출입 시 관리실 등록이 필요한 건물인지 여부</li>
<li><strong>엘리베이터·계단</strong>: 이용 가능한 동선과 위치</li>
<li><strong>야간 출입</strong>: 야간에 공동현관이나 출입문 운영 방식이 달라지는 경우 사전 안내</li>
</ul>
<p>방문 지역별 안내는 <a href="/sangnok-gu/">상록구 출장마사지 안내</a>와 <a href="/danwon-gu/">단원구 출장마사지 안내</a>에서도 확인하실 수 있습니다.</p>
</section>

<section>
<h2>추가 이동비 기준</h2>
<p>기본 방문 지역을 벗어나 외곽이거나 이동 거리가 긴 경우, 또는 심야 시간대에는 추가 이동비가 발생할 수 있습니다. 추가비가 적용되는 경우에는 예약 상담 단계에서 미리 안내해 드리므로, 방문 후에 예상치 못한 비용이 청구되는 일은 없습니다. 정확한 기준은 방문지 주소를 알려주시면 <a href="tel:0508-202-4719">0508-202-4719</a>에서 안내해 드립니다.</p>
</section>

<section>
<h2>건전한 서비스 원칙</h2>
<p>간다GO는 다음과 같은 원칙으로 서비스를 제공합니다:</p>
<ol>
<li><strong>법적 준수</strong>: 모든 서비스는 관계 법령을 준수합니다</li>
<li><strong>안전성</strong>: 고객과 직원의 안전을 최우선으로</li>
<li><strong>위생 관리</strong>: 철저한 위생 기준 유지</li>
<li><strong>신뢰성</strong>: 약속된 시간과 장소에서 정확한 서비스 제공</li>
<li><strong>거절 권리</strong>: 불합리한 요청에 대한 정중한 거절</li>
</ol>
</section>

<section>
<h2>서비스 가능 범위</h2>
<p><strong>간다GO에서 제공하는 서비스는 다음과 같습니다:</strong></p>
<ul>
<li>근육 이완 마사지</li>
<li>혈액 순환 개선 마사지</li>
<li>스트레스 해소 마사지</li>
<li>피로 회복 마사지</li>
<li>건강 관리 서비스</li>
</ul>
<p>모든 서비스는 건강과 웰니스를 목표로 하며, 의료 행위는 포함되지 않습니다.</p>
</section>

<section>
<h2>서비스 불가 사항</h2>
<p><strong>다음과 같은 경우는 서비스를 제공할 수 없습니다:</strong></p>
<ul>
<li>불법적인 요청</li>
<li>성적인 서비스 요청</li>
<li>약물 관련 요청</li>
<li>기타 법적 문제가 될 수 있는 행동</li>
</ul>
<p>이러한 요청 시 즉시 서비스를 중단하며, 경찰에 신고할 수 있습니다.</p>
</section>

<section>
<h2>위생 기준</h2>
<p><strong>간다GO는 다음의 위생 기준을 유지합니다:</strong></p>
<ul>
<li>모든 직원은 정기적인 건강 검진 실시</li>
<li>사용 도구는 매번 소독 및 세정</li>
<li>손 세정 및 위생 관리 철저</li>
<li>마스크 착용 및 개인 위생 관리</li>
<li>고객 안전을 위한 위생 프로토콜 준수</li>
</ul>
</section>

<section>
<h2>개인정보 보호</h2>
<p><strong>간다GO는 고객의 개인정보를 철저히 보호합니다:</strong></p>
<ul>
<li>예약 정보는 예약 목적으로만 사용</li>
<li>개인정보는 제3자와 공유하지 않음</li>
<li><a href="/support/privacy/">개인정보처리방침</a> 준수</li>
<li>고객 비밀 유지</li>
</ul>
</section>

<section>
<h2>문제 발생 시 처리</h2>
<p><strong>서비스 이용 중 문제가 발생한 경우:</strong></p>
<ol>
<li>즉시 서비스를 중단합니다</li>
<li>고객의 의견을 듣고 성실하게 처리합니다</li>
<li>필요한 경우 재서비스를 제공합니다</li>
<li>반복되는 문제는 <a href="/support/">고객센터</a>에 보고합니다</li>
</ol>
</section>

<section>
<h2>고객 책임</h2>
<p><strong>고객님께서 지켜주셔야 할 사항:</strong></p>
<ul>
<li>예약된 시간에 도착하여 대기</li>
<li>예약 정보의 정확한 제공</li>
<li>서비스 중 직원 존중</li>
<li>불가능한 요청 자제</li>
<li>계약된 요금 정확히 지불</li>
</ul>
</section>

<section>
<h2>이용 에티켓 안내</h2>
<p>관리사가 편안하게 방문 관리에 집중할 수 있도록 아래와 같은 기본 에티켓을 지켜 주시면 감사하겠습니다. 서로에 대한 존중은 더 나은 서비스로 이어집니다.</p>
<ul>
<li>예약 시간에 맞춰 방문지에서 대기</li>
<li>음주 상태에서의 이용 자제</li>
<li>관리에 적합하도록 공간을 미리 정리</li>
<li>관리사에 대한 존중과 예의 유지</li>
<li>불법·선정적 요청 금지 (위반 시 즉시 중단)</li>
</ul>
</section>

<section>
<h2>방문 전 확인 체크리스트</h2>
<p>방문 당일 헷갈리지 않도록 아래 항목을 한 번씩 점검해 보세요. 이 체크리스트만 확인해도 대부분의 불편을 미리 막을 수 있습니다.</p>
<ol>
<li>정확한 도로명 주소와 동·호수를 안내했는가</li>
<li>공동현관 비밀번호 또는 출입 방법을 전달했는가</li>
<li>희망 방문 시간과 이용 시간이 확정되었는가</li>
<li>결제 방식(현금·카드 등)을 확인했는가</li>
<li>건강 상의 특이사항이 있다면 미리 알렸는가</li>
<li>관리 받을 공간이 정리되어 있는가</li>
</ol>
</section>

<section>
<h2>이용 전 확인 자주 묻는 질문</h2>
<dl class="faq-list">
<dt>공동현관 비밀번호를 꼭 알려줘야 하나요?</dt>
<dd>아파트나 오피스텔처럼 공동현관이 잠겨 있는 건물이라면, 비밀번호나 세대 호출 방법을 알려주셔야 관리사가 지체 없이 방문할 수 있습니다.</dd>
<dt>관리실에 등록해야 출입할 수 있는 건물인데 어떻게 하나요?</dt>
<dd>관리실 등록이 필요한 건물이라면 예약 시 미리 말씀해 주세요. 방문자 등록 방식에 맞춰 출입을 안내해 드립니다.</dd>
<dt>추가 이동비가 갑자기 청구될 수도 있나요?</dt>
<dd>아닙니다. 추가 이동비가 발생하는 경우 예약 상담 단계에서 반드시 사전에 안내합니다.</dd>
<dt>건강 상태가 좋지 않은데 이용해도 되나요?</dt>
<dd>특이사항이 있으시면 예약 시 미리 알려주세요. 상태에 따라 적합한 방식으로 안내해 드립니다.</dd>
</dl>
</section>

<section>
<h2>문의</h2>
<p>이용 전 확인사항에 대해 더 알고 싶으시면 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하시거나, <a href="/guide/">홈타이 이용 가이드</a>와 <a href="/support/">고객센터</a> 페이지를 참고해 주세요.</p>
</section>
"""
)

guide = create_info_page(
    path="guide/",
    title="홈타이 이용 가이드｜안산 출장마사지 서비스 설명",
    desc="홈타이 서비스의 개념, 종류, 이용 방법을 안내합니다.",
    h1="홈타이 이용 가이드",
    breadcrumb=[("안산", "/"), ("이용 가이드", "")],
    body_content="""
<section>
<h2>출장마사지·홈타이란?</h2>
<p><strong>출장마사지</strong>와 <strong>홈타이</strong>는 고객이 머무는 자택·오피스텔·숙소로 관리사가 직접 방문하여 진행하는 방문형 관리 서비스입니다. 매장을 직접 찾아가지 않아도 되므로 이동 시간이 들지 않고, 익숙한 공간에서 편안하게 휴식과 피로 회복에 집중할 수 있다는 점이 가장 큰 특징입니다. 간다GO는 안산시 전역을 대상으로 건전한 방문 관리 서비스를 제공하며, 처음 이용하시는 분도 부담 없이 시작할 수 있도록 단계별로 안내해 드립니다.</p>
<p>이 가이드는 서비스 개념부터 진행 흐름, 장소별 안내, 주의사항까지 한 번에 정리한 페이지입니다. 예약 절차는 <a href="/reservation/">안산 출장마사지 예약 안내</a>에서, 방문 전 점검 사항은 <a href="/check/">이용 전 확인사항</a>에서 함께 확인하실 수 있습니다.</p>
</section>

<section>
<h2>방문형 서비스의 장점</h2>
<p>매장 방문형과 비교해 방문형 관리 서비스가 가지는 장점은 분명합니다. 무엇보다 익숙한 공간에서 이동 부담 없이 휴식에 집중할 수 있다는 점이 큰 매력입니다.</p>
<ul>
<li><strong>편의성</strong>: 자택·숙소에서 별도 이동 없이 편하게 이용</li>
<li><strong>프라이버시</strong>: 개인 공간에서 진행되어 사생활이 보호됨</li>
<li><strong>시간 절약</strong>: 오가는 이동 시간이 들지 않음</li>
<li><strong>맞춤 진행</strong>: 컨디션과 원하는 부위에 맞춘 진행</li>
<li><strong>편안한 환경</strong>: 가장 익숙한 공간에서 휴식과 피로 회복</li>
</ul>
</section>

<section>
<h2>홈타이 서비스 종류</h2>
<p><strong>간다GO에서 제공하는 주요 서비스:</strong></p>
<ul>
<li><strong>타이 마사지</strong>: 전통 태국식 마사지 기법</li>
<li><strong>스웨디시 마사지</strong>: 근육 이완과 혈액 순환 개선</li>
<li><strong>아로마테라피</strong>: 향기를 이용한 치료</li>
<li><strong>릴렉싱 마사지</strong>: 스트레스 해소 서비스</li>
<li><strong>풀바디 마사지</strong>: 전신 마사지</li>
</ul>
</section>

<section>
<h2>방문형 서비스 진행 흐름</h2>
<p>처음 이용하시는 분도 흐름만 알면 어렵지 않습니다. 간다GO의 방문 관리 서비스는 아래 순서로 진행됩니다.</p>
<ol>
<li><strong>전화 상담</strong>: <a href="tel:0508-202-4719">0508-202-4719</a>로 방문 지역·시간·이용 시간을 상담</li>
<li><strong>정보 제공</strong>: 정확한 주소와 건물 출입 방법, 희망 서비스 안내</li>
<li><strong>예약 확정</strong>: 방문 시간과 내용을 재확인하여 일정 확정</li>
<li><strong>관리사 방문</strong>: 약속된 시간에 방문지로 도착</li>
<li><strong>관리 진행</strong>: 컨디션과 원하는 부위를 확인한 뒤 관리 시작</li>
<li><strong>결제</strong>: 관리 완료 후 현장에서 결제</li>
</ol>
</section>

<section>
<h2>장소별 이용 안내</h2>
<p>방문형 서비스는 공간에 따라 준비할 점이 조금씩 다릅니다. 아래 안내를 참고하시면 어디서든 편안하게 이용하실 수 있습니다.</p>
<ul>
<li><strong>자택(아파트·주택)</strong>: 공동현관 출입 방법을 미리 전달하고, 관리 받을 공간을 가볍게 정리해 두면 좋습니다.</li>
<li><strong>오피스텔</strong>: 관리실 방문자 등록이 필요한 경우가 있으므로 출입 절차를 사전에 확인해 주세요.</li>
<li><strong>숙소·호텔</strong>: 건물명과 객실 번호를 정확히 안내하면 도착이 수월합니다.</li>
</ul>
<p>지역별 상세 안내는 <a href="/sangnok-gu/">상록구 출장마사지 안내</a>, <a href="/danwon-gu/">단원구 출장마사지 안내</a>와 <a href="/station/sangnoksu-station/">상록수역</a> 등 주요 역 페이지에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>처음 이용자를 위한 단계별 가이드</h2>
<p>방문형 서비스가 처음이라면 아래 순서대로만 따라오시면 됩니다.</p>
<ol>
<li>먼저 <a href="/reservation/">예약 안내</a>를 읽고 필요한 정보를 정리합니다.</li>
<li>전화로 방문 지역·시간·이용 시간을 상담하고 예약을 확정합니다.</li>
<li><a href="/check/">이용 전 확인사항</a>의 체크리스트로 주소와 출입 방법을 점검합니다.</li>
<li>방문 시간에 맞춰 공간을 정리하고 편안한 복장으로 대기합니다.</li>
<li>관리 후 결제를 마치고, 충분한 수분 섭취와 휴식으로 마무리합니다.</li>
</ol>
</section>

<section>
<h2>최고의 경험을 위한 준비</h2>
<p><strong>홈타이 서비스를 받기 전에 준비하세요:</strong></p>
<ul>
<li>편안한 복장 준비</li>
<li>마사지 공간 정리 (침대 또는 매트)</li>
<li>따뜻한 물과 수건 준비</li>
<li>실내 온도 조절 (24~25도 권장)</li>
<li>휴대폰 무음 설정</li>
<li>마사지 받을 부위 확인</li>
</ul>
</section>

<section>
<h2>이용 중 주의사항</h2>
<p>편안하고 안전한 이용을 위해 아래 사항을 기억해 주세요. 작은 점검이 더 좋은 컨디션과 만족도로 이어집니다.</p>
<ul>
<li>관리사의 안내에 따라 자세를 편하게 유지하기</li>
<li>불편하거나 통증이 느껴지면 즉시 알리기</li>
<li>이용 전 과도한 음주 자제하기</li>
<li>지병이나 부상이 있으면 시작 전 미리 알리기</li>
<li>지나치게 강한 압을 요청하지 않기</li>
<li>불법·선정적 요청은 불가하다는 점을 이해하기 (자세한 기준은 <a href="/check/">이용 전 확인사항</a> 참고)</li>
</ul>
</section>

<section>
<h2>마사지 후 관리</h2>
<p><strong>서비스 후 빠른 회복을 위해:</strong></p>
<ul>
<li>따뜻한 물로 가볍게 씻기</li>
<li>수분 섭취 충분히 하기</li>
<li>2시간 이상 찬바람 피하기</li>
<li>과도한 활동 자제</li>
<li>푹신한 베개 사용</li>
</ul>
</section>

<section>
<h2>이용 가이드 자주 묻는 질문</h2>
<dl class="faq-list">
<dt>홈타이와 출장마사지는 무엇이 다른가요?</dt>
<dd>둘 다 관리사가 고객의 공간으로 방문하는 방문형 서비스를 가리키는 말로, 큰 틀에서는 같은 개념입니다. 간다GO에서는 자택·오피스텔·숙소 어디든 방문 일정을 조율할 수 있습니다.</dd>
<dt>매주 정기적으로 이용할 수 있나요?</dt>
<dd>네. 원하시는 요일과 시간대를 말씀해 주시면 정기 방문 일정으로 조율해 드립니다.</dd>
<dt>건강 상의 특이사항이 있어도 이용할 수 있나요?</dt>
<dd>예약 시 미리 알려주시면 상태에 맞는 방식으로 안내해 드립니다. 컨디션이 좋지 않은 날에는 무리하지 않으시길 권합니다.</dd>
<dt>방문 전에 무엇을 준비하면 되나요?</dt>
<dd>관리 받을 공간을 가볍게 정리하고, 편안한 복장과 수건을 준비해 두시면 충분합니다. 자세한 내용은 <a href="/check/">이용 전 확인사항</a>을 참고하세요.</dd>
</dl>
</section>

<section>
<h2>문의</h2>
<p>출장마사지·홈타이 서비스에 대해 더 알고 싶으시면 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하시거나, <a href="/reservation/">예약 안내</a>와 <a href="/support/">고객센터</a> 페이지를 참고해 주세요.</p>
</section>
"""
)

privacy = create_info_page(
    path="support/privacy/",
    title="개인정보처리방침｜안산 출장마사지 개인정보 보호",
    desc="간다GO의 개인정보 수집, 이용, 보호 정책을 안내합니다.",
    h1="개인정보처리방침",
    breadcrumb=[("안산", "/"), ("고객센터", "/support/"), ("개인정보처리방침", "")],
    body_content="""
<section>
<h2>개인정보처리방침 개요</h2>
<p><strong>간다GO</strong>는 고객의 개인정보를 소중히 여기며, 개인정보 보호법을 준수하여 고객의 개인정보를 안전하게 관리합니다.</p>
</section>

<section>
<h2>수집하는 개인정보</h2>
<p><strong>예약 시 수집하는 정보:</strong></p>
<ul>
<li>이름</li>
<li>전화번호</li>
<li>서비스 주소</li>
<li>예약 시간</li>
<li>서비스 요청사항</li>
</ul>
<p><strong>선택적 정보:</strong></p>
<ul>
<li>이메일 주소</li>
<li>특별 건강 상태 정보</li>
</ul>
</section>

<section>
<h2>개인정보 이용 목적</h2>
<p>수집된 개인정보는 다음 목적으로만 사용됩니다:</p>
<ul>
<li>예약 확인 및 서비스 제공</li>
<li>고객 연락 및 상담</li>
<li>서비스 개선</li>
<li>법적 요구사항 충족</li>
<li>분쟁 해결</li>
</ul>
</section>

<section>
<h2>개인정보 보관 기간</h2>
<ul>
<li><strong>기본 보관</strong>: 서비스 제공 종료 후 1년</li>
<li><strong>법적 보관</strong>: 관계 법령 요구 시 해당 기간</li>
<li><strong>고객 요청</strong>: 삭제 요청 시 즉시 삭제</li>
</ul>
</section>

<section>
<h2>개인정보 보안</h2>
<p><strong>간다GO는 다음과 같이 개인정보를 보호합니다:</strong></p>
<ul>
<li>암호화 통신</li>
<li>접근 제한</li>
<li>정기적인 보안 감시</li>
<li>직원 교육 및 서명</li>
<li>물리적 보안 조치</li>
</ul>
</section>

<section>
<h2>개인정보 제3자 공유</h2>
<p><strong>간다GO는 다음과 같은 경우를 제외하고 개인정보를 제3자와 공유하지 않습니다:</strong></p>
<ul>
<li>고객의 명시적인 동의</li>
<li>법적 요구 (경찰, 검찰, 법원)</li>
<li>서비스 제공을 위한 필수적인 경우</li>
</ul>
</section>

<section>
<h2>고객의 권리</h2>
<p><strong>고객님은 다음의 권리가 있습니다:</strong></p>
<ul>
<li><strong>열람권</strong>: 자신의 개인정보 열람 요청</li>
<li><strong>정정권</strong>: 잘못된 정보 수정 요청</li>
<li><strong>삭제권</strong>: 개인정보 삭제 요청</li>
<li><strong>처리 정지권</strong>: 개인정보 처리 중단 요청</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a>로 요청하실 수 있습니다.</p>
</section>

<section>
<h2>쿠키와 추적 기술</h2>
<p>간다GO 웹사이트는 사용자 경험 개선을 위해 쿠키를 사용할 수 있습니다. 쿠키는 언제든 브라우저 설정에서 비활성화할 수 있습니다.</p>
</section>

<section>
<h2>정책 변경</h2>
<p>이 개인정보처리방침은 예고 없이 변경될 수 있습니다. 변경 시 웹사이트를 통해 공지합니다.</p>
</section>

<section>
<h2>문의</h2>
<p><strong>개인정보에 대한 문의:</strong></p>
<ul>
<li><strong>전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a></li>
<li><strong>상담 시간</strong>: 연중무휴 24시간</li>
<li><strong>텔레그램</strong>: <a href="https://t.me/googleseolab">@googleseolab</a></li>
</ul>
</section>

<section>
<h2>정책 동의</h2>
<p>서비스 예약 및 이용으로 본 개인정보처리방침에 동의하는 것으로 간주됩니다.</p>
</section>
"""
)

support = create_info_page(
    path="support/",
    title="고객센터｜안산 출장마사지 문의 및 지원",
    desc="간다GO 고객센터 연락처, 문의 방법, 피드백을 안내합니다.",
    h1="고객센터",
    breadcrumb=[("안산", "/"), ("고객센터", "")],
    body_content="""
<section>
<h2>고객센터 안내</h2>
<p><strong>간다GO</strong>는 24시간 고객 상담을 제공합니다. 예약, 서비스, 기술적 문제 등 모든 사항에 대해 도움을 드릴 준비가 되어 있습니다.</p>
</section>

<section>
<h2>연락처</h2>
<ul>
<li><strong>회사명</strong>: 간다GO</li>
<li><strong>예약 및 상담 전화</strong>: <a href="tel:0508-202-4719">0508-202-4719</a></li>
<li><strong>상담 시간</strong>: 연중무휴 24시간 운영</li>
<li><strong>서비스 지역</strong>: 경기도 안산시 전지역</li>
</ul>
</section>

<section>
<h2>기타 연락 방법</h2>
<ul>
<li><strong>텔레그램</strong>: <a href="https://t.me/googleseolab">@googleseolab</a></li>
<li><strong>웹사이트</strong>: ansan-massage1.pages.dev</li>
</ul>
</section>

<section>
<h2>문의 사항 안내</h2>
<p>고객센터로 다음 사항들을 문의할 수 있습니다:</p>
<ul>
<li><strong>예약</strong>: <a href="/reservation/">예약 안내</a> 참조</li>
<li><strong>취소</strong>: 예약된 서비스 취소</li>
<li><strong>변경</strong>: 예약 시간 또는 내용 변경</li>
<li><strong>불만사항</strong>: 서비스 이용 중 문제</li>
<li><strong>기술 지원</strong>: 웹사이트 이용 문제</li>
<li><strong>제휴 및 협력</strong>: 비즈니스 제안</li>
<li><strong>기타</strong>: 모든 관련 문의</li>
</ul>
</section>

<section>
<h2>불만 처리 절차</h2>
<ol>
<li><strong>접수</strong>: 전화 또는 온라인으로 불만 접수</li>
<li><strong>조사</strong>: 상황 파악 및 원인 분석</li>
<li><strong>응답</strong>: 24시간 내 초기 응답</li>
<li><strong>해결</strong>: 적절한 조치 및 해결</li>
<li><strong>확인</strong>: 고객 만족도 확인</li>
</ol>
</section>

<section>
<h2>서비스 개선 피드백</h2>
<p>간다GO는 고객의 의견을 소중히 여깁니다. 서비스 개선을 위한 모든 제안과 피드백을 환영합니다:</p>
<ul>
<li>좋았던 점 공유</li>
<li>개선할 사항 제안</li>
<li>새로운 서비스 아이디어</li>
<li>기타 건설적인 의견</li>
</ul>
</section>

<section>
<h2>자주 묻는 질문</h2>
<ul>
<li><strong>Q: 긴급 상황 발생 시 어떻게 하나요?</strong>
  <br>A: 즉시 전화로 연락 주세요. 긴급 상황은 우선 처리됩니다.</li>
<li><strong>Q: 야간에 연락할 수 있나요?</strong>
  <br>A: 네, 24시간 상담이 가능합니다.</li>
<li><strong>Q: 회사 정보를 알고 싶어요.</strong>
  <br>A: 전화로 상세한 정보를 제공합니다.</li>
</ul>
</section>

<section>
<h2>다른 지원</h2>
<p><strong>기타 도움이 필요한 사항:</strong></p>
<ul>
<li><a href="/check/">이용 전 확인사항</a> — 안전 가이드</li>
<li><a href="/guide/">홈타이 이용 가이드</a> — 서비스 설명</li>
<li><a href="/support/privacy/">개인정보처리방침</a> — 개인정보 보호</li>
<li><a href="/">메인 페이지</a> — 전체 정보</li>
</ul>
</section>

<section>
<h2>웹사이트 제작 문의</h2>
<p>이 웹사이트 제작에 관심이 있으시면 <a href="https://t.me/googleseolab">텔레그램</a>으로 문의하시기 바랍니다.</p>
</section>

<section>
<h2>제휴 및 협력</h2>
<p><strong>간다GO와의 제휴 및 협력을 원하시면:</strong></p>
<p><a href="https://t.me/googleseolab">Telegram: @googleseolab</a></p>
<p>또는 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락 주세요.</p>
</section>
"""
)

# PAGES 리스트에 모든 정보 페이지 집계
PAGES = [
    reservation,
    check,
    guide,
    privacy,
    support,
]
