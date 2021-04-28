import streamlit as st
#mport numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title("超入門")


st.write("プログレスバーの表示")
st.write("インタラクティブなWidgets")

"Start!!"

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)






left_column,right_column=st.beta_columns(2)


button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右")

expander=st.beta_expander("問い合わせ")
expander.write("内容を書く")
expander.write("内容を書く")
expander.write("内容を書く")
expander.write("内容を書く")



option=st.selectbox(
    "好きな数字は",
    list(range(1,11))
)
"あなたの数字は",option,"です"


text=st.text_input("趣味は")
"あなたの趣味は",text,"です"


conditon=st.slider("調子は",0,100,50)
"コンディション",conditon



# if st.checkbox("show Image"):
#    img=Image.open("34528.jpg")
#    st.image(img,caption="food",use_column_width=True) """



