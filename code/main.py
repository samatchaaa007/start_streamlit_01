import streamlit as st
from my_pages import page1, page2, page3  # ✅ Import แบบถูกต้อง

st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("เลือกหน้า", ["Page 1", "Page 2", "Page 3"])  # ✅ เปลี่ยนจาก page_link เป็น selectbox

st.title(page)

# ✅ ใช้ dictionary mapping ที่ถูกต้อง
page_mapping = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3
}

# ✅ เรียกใช้ show() จาก module ที่เลือก
if page in page_mapping:
    page_mapping[page].show()
