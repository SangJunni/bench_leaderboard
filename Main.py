import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to BenchMark Viewer!! 👋")

st.markdown(
    """
- 위 프로젝트는 직접 개발한 LLM 모델들의 성능 수치를 시각화하기 위해서 만든 벤치마크 리더보드 시각화 페이지입니다.
### 활용방법
1. 멀티 페이지로 구성되었기 때문에 레포지토리 내부의 pages에 새로운 벤치마크 통계 코드를 추가합니다.
2. 각 벤치마크에 대한 모델 결과를 저장하기 위한 별도의 폴더를 생성.
3. 각 모델의 벤치마크 테스트 결과를 폴더에 저장
4. 데이터 프레임의 열을 클릭하여 각 항목 별 오름차순, 내림차순 결과 확인

### 현재 추가된 벤치마크
1. [MT-Bench](https://lk.instruct.kr/)
    : 외국어 MT-Bench를 참고하여 제작된 다분야 사고력 벤치마크(추론, 수학, 글쓰기, 코딩, 이해, 문법, 싱글턴, 멀티턴에 대하여 평가 진행)
2. 추가예정
"""
)