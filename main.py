import streamlit as st
import numpy as np
import pandas as pd

st.title("超入門")

st.write("DataFrame")

#df=pd.DataFrame({
#    "1列目":[1,2,3,4],
#    "2列目":[10,20,30,40]
#})

#st.write(df)
#st.table(df.style.highlight_max(axis=0))#スタティックなテーブル
#st.dataframe(df.style.highlight_max(axis=0),width=500,height=500)#動的なテーブル

"""
# 章
## 節
### 項

```pyton 
import streamlit as st
import numpy as numpy
import pandas as pd
```
"""
"""
df=pd.DataFrame(np.random.rand(20, 3),columns=["a","b","c"])
st.line_chart(df)
"""


df=pd.DataFrame(
    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]
    )

st.map(df)

from PIL import Image
img=Image.open("34528.jpg")

st.image(img,caption="food",use_column_width=True)