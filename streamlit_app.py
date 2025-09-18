import streamlit as st

st.title('Streamlit 요소 데모')

st.header('텍스트 요소')
st.write('이것은 일반 텍스트입니다.')
st.markdown('**마크다운** _스타일_')
st.code('print("Hello, Streamlit!")', language='python')

st.header('입력 요소')
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이', min_value=0, max_value=120, value=25)
agree = st.checkbox('동의합니다')

st.header('버튼')
if st.button('클릭!'):
    st.success('버튼이 클릭되었습니다!')

st.header('슬라이더')
value = st.slider('값을 선택하세요', 0, 100, 50)
st.write(f'선택한 값: {value}')

st.header('선택박스')
option = st.selectbox('옵션을 선택하세요', ['A', 'B', 'C'])
st.write(f'선택한 옵션: {option}')

st.header('이미지')
st.image('https://static.streamlit.io/examples/dog.jpg', caption='강아지 이미지', use_column_width=True)

st.header('데이터프레임')
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
