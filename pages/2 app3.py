import streamlit as st
import pandas as pd  # st은 입력과 출력만 담당할 뿐 실제 로직은 나머지 파이썬 코드로 구현됩니다.

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


# 입력
st.title('1. 입력버튼들')

button_result = st.button('Hit me')
# 버튼을 누르면 데이터프레임이 등장하도록 로직을 만들어주세요
if button_result == True:
    st.write(button_result)
    st.data_editor(data)

check_result = st.checkbox('Check me out')
if check_result == True:
    st.data_editor(data)

st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,2,3])

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

search = st.text_input('Enter some text')
for ani_ in ani_list:
    if search in ani_:
        img_idx = ani_list.index(ani_)

if search != '':
    st.image(img_list[img_idx])

st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button(
    label="Download data as CSV",
    data=data.to_csv(),
    file_name='app_df.csv',
    mime='text/csv'
)
picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
    
st.color_picker('Pick a color')

# 출력
st.title('2. 출력메서드들')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #(제목 마크다운) _(기울임 마크다운) *(굵기 마크다운)
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''') # 수식 입력기
st.write(data) # df, err, func, keras! 안에 있는 데이터를 파이썬 코드로 읽어서 실행
st.write(['st', 'is <', 3]) # see * 리스트 자료형으로 읽어서 출력
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()') # 코드블럭 작성

# * optional kwarg unsafe_allow_html = True

# 출력
