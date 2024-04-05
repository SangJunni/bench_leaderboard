import jsonlines
import streamlit as st
import pandas as pd
import os
import json

# Streamlit 앱의 타이틀 설정
st.title('Bench Result')

# 폴더 경로 설정 (모델별 JSON 파일이 있는 폴더를 가정합니다. 실제 경로에 맞게 수정하세요.)
folder_path = 'test_result'

# 해당 폴더 내의 모든 JSON 파일을 리스트업
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 모든 JSON 파일에서 데이터를 읽어서 하나의 데이터프레임으로 만들기
all_models_scores = []

for file in files:
    category_scores = {}
    query_single_scores = []
    query_multi_scores = []
    file_path = os.path.join(folder_path, file)
    # 모델명 추출 (파일명에서 확장자 제거)
    model_name = os.path.splitext(file)[0][6:]
    model = {"모델명": model_name}
    with jsonlines.open(file_path) as f:  # 인코딩을 utf-8로 명시
        for line in f:
             # JSON 객체로 변환
            data = line
            # 카테고리 추출
            category = data['category']
            # 각 카테고리별로 점수 리스트에 추가
            if category not in category_scores:
                category_scores[category] = []
            category_scores[category].append(data['query_single']['judge_score'])
            category_scores[category].append(data['query_multi']['judge_score'])
            # 전체 query_single과 query_multi 점수를 리스트에 추가
            query_single_scores.append(data['query_single']['judge_score'])
            query_multi_scores.append(data['query_multi']['judge_score'])
        category_average_scores = {cat: sum(scores)/len(scores) for cat, scores in category_scores.items()}
        average_query_single = sum(query_single_scores) / len(query_single_scores)
        average_query_multi = sum(query_multi_scores) / len(query_multi_scores)
        average_total = (average_query_single + average_query_multi)/2

#     # 모델명을 데이터에 추가
    category_average_scores["싱글턴"] = average_query_single
    category_average_scores["멀티턴"] = average_query_multi
    category_average_scores["총합"] = average_total
    model.update(category_average_scores)
    all_models_scores.append(model)

# 데이터프레임 생성
df = pd.DataFrame(all_models_scores)

# Streamlit에 테이블 형식으로 데이터 표시
st.table(df)

# TODO: CML에서 작동하도록 설정하기
# https://github.com/cloudera/CML_AMP_Streamlit_on_CML/blob/master/cml/launch_app.py