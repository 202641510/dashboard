# 📚 공부 습관 대시보드 (Study Habit Dashboard)

Streamlit과 Pandas를 활용하여 학생들의 공부 시간 및 성적 데이터를 한눈에 파악할 수 있는 대시보드 웹 애플리케이션입니다.

---

## 🛠️ 기능 (Features)

- **요약 지표 (Metrics)**: 총 학생 수, 평균 점수, 평균 공부 시간을 한줄로 한눈에 확인
- **데이터 필터링 (Slider)**: 최소 공부 시간을 슬라이더로 설정하여 조건에 맞는 학생만 필터링
- **기본 시각화 (Charts)**:
  - 공부 시간과 점수 간의 관계를 보여주는 **산점도 (Scatter Chart)**
  - 필터링된 학생별 점수를 비교하는 **막대그래프 (Bar Chart)**

---

## 📁 파일 구조 (Directory Structure)

```text
.
├── app.py          # Streamlit 대시보드 메인 코드
├── study.csv       # 학생 데이터 파일 (선택 사항)
└── README.md       # 프로젝트 설명서