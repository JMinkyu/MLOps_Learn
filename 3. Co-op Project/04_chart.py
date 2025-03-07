import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('04_chart')
st.write("") # 간격 벌리기

# 시각화를 캔버스 안에다가 수행
#  캔버스 안에 있는 그래프 -> figure
# figure를 스트림릿으로 표현

# DataFrame 생성

code = """
data = pd.DataFrame({
    'name': ['a', 'b', 'c'],
    'age': [22, 31, 25],
    'weight': [75.5, 80.2, 55.1]
})
"""

data = pd.DataFrame({
    'name': ['a', 'b', 'c'],
    'age': [22, 31, 25],
    'weight': [75.5, 80.2, 55.1]
})

st.code(code)

st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(data['name'], data['age'])
st.pyplot(fig)

# Seaborn은 시각화의 결과가 바로 figure가 된다.
bar_seaborn = sns.barplot(data=data, 
                          x='name', 
                          y='age', 
                          palette='Set2')

fig = bar_seaborn.get_figure()

st.pyplot(fig)

