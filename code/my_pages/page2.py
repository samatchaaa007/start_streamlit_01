import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.write("### 🎉 ยินดีต้อนรับสู่หน้า 2")
    st.write("📌 เนื้อหาของหน้า 2")

    # ใช้ st.tabs() เพื่อสร้าง Tab Menu
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "Redeem Overall", "Earn", "Earn II", "Redeem", 
        "Redeem II", "Redeem III", "Redeem IV", "2025 Earn", "2025 Redeem"
    ])

    # ✅ ฟังก์ชันสร้าง Card (ขนาดเท่ากัน แต่ Style ต่างกัน)
    def create_card(col, value, title, bg_color, text_color, shadow_color):
        col.markdown(
            f"""
            <div style="
                background-color: {bg_color}; 
                padding: 20px; 
                border-radius: 15px; 
                text-align: center;
                height: 150px; 
                display: flex; 
                flex-direction: column; 
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                font-weight: bold;
                box-shadow: 4px 4px 10px {shadow_color};
            ">
                <h1 style="color: {text_color}; font-size: 36px; margin-bottom: 5px;">{value:,}</h1>
                <h3 style="color: #333; font-size: 20px;">{title}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tab1:
        st.subheader("📊 Redeem Overall")
        st.write("เนื้อหาสำหรับ Redeem Overall")

        # ✅ สร้าง DataFrame ตัวอย่าง
        data = {
            "Category": ["A", "B", "C", "D", "E", "F", "G", "H"],
            "Value": [100, 200, 150, 300, 250, 356, 789, 670],
            "Region": ["North", "South", "East", "West", "North", "East", "West", "North"]
        }
        df = pd.DataFrame(data)

        # ✅ คำนวณผลรวมของแต่ละ Region
        df_region_sum = df.groupby("Region")["Value"].sum().reset_index()

        # ✅ ดึงค่าผลรวมของแต่ละ Region
        north_total = df_region_sum[df_region_sum["Region"] == "North"]["Value"].sum()
        south_total = df_region_sum[df_region_sum["Region"] == "South"]["Value"].sum()
        east_total = df_region_sum[df_region_sum["Region"] == "East"]["Value"].sum()
        west_total = df_region_sum[df_region_sum["Region"] == "West"]["Value"].sum()

        # ✅ แสดงผลใน Card (เชื่อมกับค่าผลรวมของแต่ละ Region)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            create_card(col1, north_total, "North", "#FFCDD2", "#B71C1C", "rgba(183,28,28,0.2)")  # สีแดงอ่อน

        with col2:
            create_card(col2, south_total, "South", "#C8E6C9", "#1B5E20", "rgba(27,94,32,0.2)")  # สีเขียวอ่อน

        with col3:
            create_card(col3, east_total, "East", "#BBDEFB", "#0D47A1", "rgba(13,71,161,0.2)")  # สีฟ้าอ่อน

        with col4:
            create_card(col4, west_total, "West", "#FFF9C4", "#FF6F00", "rgba(255,111,0,0.2)")  # สีเหลืองอ่อน

        # ✅ เพิ่ม Sidebar Filter
        st.sidebar.header("🔍 Filter Data")
        filter_region = st.sidebar.multiselect("🌎 เลือก Region", df["Region"].unique(), default=df["Region"].unique())

        # ✅ Apply Filter
        df_filtered = df[df["Region"].isin(filter_region)]

        # ✅ ปรับ Layout: ให้ Table และ Graph กว้างเท่ากัน
        col_table, col_chart = st.columns([1, 1])  # แบ่ง 50-50

        with col_table:
            st.subheader("📋 ข้อมูลตาราง")
            st.dataframe(df_filtered.style.format({"Value": "{:,.0f}"}), use_container_width=True)

        with col_chart:
            st.subheader("📈 กราฟแท่งข้อมูล")

            # ✅ ใช้ Plotly ปรับขนาดของ Graph ให้พอดีกับ Layout
            fig = px.bar(df_filtered, x="Category", y="Value", color="Category",
                         title="📊 Bar Chart", labels={"Value": "จำนวน", "Category": "หมวดหมู่"},
                         color_discrete_sequence=px.colors.qualitative.Set1)

            # 🔹 ปรับ Layout ของ Graph
            fig.update_layout(
                width=500,  # กำหนดขนาดให้ไม่ยืดมาก
                height=400,  # ปรับให้ Graph ไม่สูงเกินไป
                margin=dict(l=20, r=20, t=40, b=20),  # ลดระยะขอบ
                title_x=0.5  # จัด Title ให้อยู่กึ่งกลาง
            )

            st.plotly_chart(fig, use_container_width=True)

