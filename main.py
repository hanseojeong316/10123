import streamlit as st
import datetime

# 구체적인 컬러 매핑
birth_colors = {
    1: ("미드나잇 블루", "#191970", "깊고 차분한 신뢰감 있는 색"),
    2: ("아메시스트 퍼플", "#9966CC", "신비롭고 창의적인 분위기"),
    3: ("민트 그린", "#98FF98", "상쾌하고 생동감 있는 색"),
    4: ("살몬 핑크", "#FF91A4", "부드럽고 따뜻한 봄 느낌"),
    5: ("에메랄드 그린", "#50C878", "생명력 있고 고급스러운 인상"),
    6: ("스카이 블루", "#87CEEB", "청량하고 자유로운 감성"),
    7: ("루비 레드", "#9B111E", "강렬하고 열정적인 이미지"),
    8: ("코랄 오렌지", "#FF7F50", "밝고 활기찬 에너지"),
    9: ("올리브 그린", "#808000", "안정감 있고 자연 친화적인 색"),
    10: ("인디고", "#4B0082", "신비롭고 지적인 분위기"),
    11: ("마룬 와인", "#800000", "깊이 있고 성숙한 인상"),
    12: ("스노우 화이트", "#FFFAFA", "순수하고 포근한 느낌"),
}

# Streamlit 앱
st.title("🎂 생일로 알아보는 당신의 컬러")
st.write("당신의 생일에 맞는 고유한 컬러를 추천해드려요!")

birth_date = st.date_input("생일을 선택하세요", value=datetime.date(2000, 1, 1))

if birth_date:
    month = birth_date.month
    color_name, hex_code, description = birth_colors.get(month)

    # 결과 표시
    st.subheader(f"🎨 추천 색상: {color_name}")
    st.write(f"설명: {description}")
    st.write(f"HEX 코드: `{hex_code}`")

    # 색상 박스 미리보기
    st.markdown(
        f"""
        <div style='width:100%;height:120px;
                    background-color:{hex_code};
                    border-radius:10px;
                    border:2px solid #ccc;
                    margin-top:10px;'>
        </div>
        """,
        unsafe_allow_html=True
    )
