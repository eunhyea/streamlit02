import streamlit as st

# Using object notation
# sidebar : 사이드바
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    # with문 안에서 동작함
    st.write(add_selectbox)
    st.write(add_radio)

# column을 (2)개 만들어서 1,2로 지정    
col1, col2 = st.columns(2)
col1.write('ddndndn 1')
col2.write('HEADER')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1])
# col1 is wider
# 3:1:1 의 비율로 나눔

# Using 'with' notation:
with col1:
    st.image('https://i.imgur.com/MDKQoDc.jpg')
with col2:
    st.image('https://i.imgur.com/t2ewhfH.png')
with col3:
    st.image('https://i.imgur.com/ECROFMC.png')


#인터렉티브한 화면을 만들어줌