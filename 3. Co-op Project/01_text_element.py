import streamlit as st

# 전체적인 문서의 제목
st.title("Hello Streamlit")

# 각 아티클의 제목
st.header("여기는 해더입니다.")
st.subheader("여기는 소제목 같은 것들을 적습니다.")

# 캡션 - 데이터프레임이나 이미지를 설명하기 위한 간단한 텍스트
st.caption("여기는 캡션입니다")

# 코드 표현
my_sample_code = """
def function_name():
    print("hello world")
"""
st.code(my_sample_code, language="python")

# 일반 텍스트
st.text("여기는 일반 텍스트입니다~~~~")

# 마크다운 입력
st.markdown("이거는 **마크다운**으로 입력된 텍스트입니다.")
st.markdown("색상을 :green[초록색]으로, :blue[**파란색이면서 굵게**] 표현!")

# Latex 문법을 Markdown으로 표현
#   - 인라인 : $수식$
st.markdown("$x^2+y^2=z^2$ 이거는 피타고라스 정리에요~~~")

# 블록 수식은 latex
st.latex("x^2+y^2=z^2")