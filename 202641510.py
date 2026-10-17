import pandas as pd
import streamlit as st

# 1. 페이지 설정 및 제목 표시
st.set_page_config(page_title="공부 습관 대시보드", layout="wide")
st.title("📚 공부 습관 대시보드")

# 2. 데이터 불러오기
# 데이터 원본이 없을 경우를 대비한 처리
try:
    df = pd.read_csv("study.csv")
except FileNotFoundError:
    # 기본 샘플 데이터 생성 (파일이 없을 경우 대비)
    data = {
        "학생ID": [f"학생_{i}" for i in range(1, 11)],
        "공부시간": [2.5, 4.0, 1.5, 5.5, 3.0, 6.0, 2.0, 4.5, 1.0, 5.0],
        "스마트폰": [3.0, 1.5, 4.0, 1.0, 2.5, 0.5, 3.5, 2.0, 5.0, 1.0],
        "점수": [70, 85, 60, 95, 75, 98, 65, 88, 50, 92],
    }
    df = pd.DataFrame(data)

# 3. 요약 지표 (st.metric) 한 줄 표시
st.subheader("📌 요약 지표")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="총 학생 수", value=f"{len(df)}명")

with col2:
    st.metric(label="평균 점수", value=f"{df['점수'].mean():.1f}점")

with col3:
    st.metric(label="평균 공부 시간", value=f"{df['공부시간'].mean():.1f}시간")

st.divider()

# 4. 최소 공부 시간 슬라이더 필터링 설정
st.subheader("🔍 데이터 필터링 및 시각화")
min_hours = float(df["공부시간"].min())
max_hours = float(df["공부시간"].max())

selected_hours = st.slider(
    "최소 공부 시간을 선택하세요 (시간)",
    min_value=min_hours,
    max_value=max_hours,
    value=min_hours,
    step=0.5,
)

# 선택한 최소 공부 시간 이상인 학생 데이터만 필터링
filtered_df = df[df["공부시간"] >= selected_hours]

# 5. 차트 시각화 (Streamlit 기본 차트 사용)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.write("### 📈 공부 시간 vs 점수 (산점도)")
    # Streamlit 기본 scatter_chart 함수 사용
    st.scatter_chart(data=filtered_df, x="공부시간", y="점수")

with chart_col2:
    st.write("### 📊 학생별 점수 (막대그래프)")
    # Streamlit 기본 bar_chart 함수 사용
    st.bar_chart(data=filtered_df, x="학생ID", y="점수")