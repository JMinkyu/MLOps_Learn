import streamlit as st
import FinanceDataReader as fdr
import datetime

st.title('finance_chart ver1')


date = st.date_input(
    "조회 시작일 선택",
    datetime.datetime(2025, 1, 1)
)

code = st.text_input(
    label = "종콕코드",
    value = "",
    placeholder = "종목 코드를 입력하세요"
)

# 날짜와 코드가 잘 들어있어야 주가 조회

if code and date :
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True)
    st.dataframe(data)
    st.line_chart(data)