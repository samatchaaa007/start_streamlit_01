import streamlit as st

st.set_page_config(layout="wide")

# ตรวจสอบ Session State เพื่อเก็บค่าหน้าปัจจุบัน
if "page" not in st.session_state:
    st.session_state.page = "Page 1"

st.sidebar.title("Navigation")

# วนลูปสร้างปุ่ม 20 หน้า
for i in range(1, 21):
    if st.sidebar.button(f"Page {i}"):
        st.session_state.page = f"Page {i}"

# แสดงผลตามหน้าที่เลือก
st.title(st.session_state.page)
st.write(f"เนื้อหาสำหรับ {st.session_state.page}")
