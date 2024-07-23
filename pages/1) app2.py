import streamlit as st

# 사용자 입력 화면 - HTML/CSS/JS로 최종적으로 변환됨

# 동작
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 텍스트 입력창
title = st.text_input("검색하실 애니메이션을 입력하세요", "")

for ani_ in ani_list:
    if title in ani_:
        # ani_list에서 특정 문자열을 포함한 인덱스를 찾아서
        img_idx = ani_list.index(ani_)

if title != '':
    st.image(img_list[img_idx])

# 내코드
# if title == '짱구는못말려':
#     st.image(img_list[0])
#     st.download_button("Download file", data=img_list[0])
# elif title =='몬스터':
#     st.image(img_list[1])
#     st.download_button("Download file", data=img_list[1])
# elif title == '릭앤모티':
#     st.image(img_list[2])
#     st.download_button("Download file", data=img_list[2])


# 출력
# st.write(val1)
# st.image("./data/image1.png") # .은 자기자신, 
# 현재의 경로 윈도우는 \로 구분, 맥이나 리눅스는 /로 구분