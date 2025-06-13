import streamlit as st
import datetime

# 별자리 정의 및 성격 유형 매핑
zodiac_signs = [
    ("물병자리", (1, 20), (2, 18), "독창적이고 진보적인 사고를 가짐"),
    ("물고기자리", (2, 19), (3, 20), "감수성이 풍부하고 상상력이 뛰어남"),
    ("양자리", (3, 21), (4, 19), "도전적이고 에너지가 넘침"),
    ("황소자리", (4, 20), (5, 20), "신중하고 안정적인 성향"),
    ("쌍둥이자리", (5, 21), (6, 21), "사교적이고 호기심이 많음"),
    ("게자리", (6, 22), (7, 22), "감정적이고 보호본능이 강함"),
    ("사자자리", (7, 23), (8, 22), "자신감 있고 리더십이 강함"),
    ("처녀자리", (8, 23), (9, 22), "꼼꼼하고 분석적인 성향"),
    ("천칭자리", (9, 23), (10, 22), "균형을 중시하고 예술적인 감각이 뛰어남"),
    ("전갈자리", (10, 23), (11, 22), "열정적이고 직관이 뛰어남"),
    ("사수자리", (11, 23), (12, 24), "자유롭고 낙천적인 성격"),
    ("염소자리", (12, 25), (1, 19), "책임감이 강하고 현실적인 성격"),
]

def get_zodiac(month: int, day: int):
    for sign, start, end, personality in zodiac_signs:
        start_month, start_day = start
        end_month, end_day = end
        if (month == start_month and day >= start_day) or \
           (month == end_month and day <= end_day) or \
           (start_month > end_month and (month == start_month or month == end_month)):
            return sign, personality
    return None, "정보를 찾을 수 없습니다."

# Streamlit UI
st.title("🎂 생일로 알아보는 성격 유형")
st.write("생일을 입력하면 당신의 별자리와 성격 유형을 알려드릴게요!")

birth_date = st.date_input("생일을 선택하세요", value=datetime.date(2000, 1, 1))

if birth_date:
    sign, personality = get_zodiac(birth_date.month, birth_date.day)
    st.subheader(f"🌟 당신의 별자리는: {sign}")
    st.write(f"🧠 성격 유형: {personality}")
