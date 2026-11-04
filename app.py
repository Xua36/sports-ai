import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="陕西全民健身赛事智能服务原型",
    layout="wide"
)

st.title("陕西全民健身赛事智能服务原型")
st.caption("基于公开数据与仿真数据的可演示原型 · 结项验收版本")
st.success("✅ 数据底座已就绪，请点击左侧导航栏进入不同角色端体验。")

DATA_DIR = "data"

try:
    df_users = pd.read_csv(os.path.join(DATA_DIR, "simulated_users.csv"), encoding='gbk')
    df_events = pd.read_csv(os.path.join(DATA_DIR, "simulated_events.csv"), encoding='gbk')
    df_interactions = pd.read_csv(os.path.join(DATA_DIR, "simulated_interactions.csv"), encoding='gbk')
    
    tab1, tab2, tab3 = st.tabs(["👥 用户画像数据", "🏃 赛事名录数据", "🔗 匹配交互数据"])
    
    with tab1:
        st.table(df_users.head(20))  
    with tab2:
        st.table(df_events)
    with tab3:
        st.table(df_interactions)
        
except Exception as e:
    st.error(f"❌ 数据读取发生异常: {e}")