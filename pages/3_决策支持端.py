import streamlit as st
import pandas as pd

st.title("🏛️ 体育主管部门决策支持端")
st.write("基于平台运行数据与公开宏观数据，为区域全民健身布局提供决策依据。")

st.subheader("📈 陕西省全民健身核心指标（宏观公开数据）")
col1, col2, col3 = st.columns(3)
col1.metric("全省经常锻炼人口占比", "45%", "稳步提升")
col2.metric("人均体育场地面积", "2.62 ㎡")
col3.metric("2024年举办赛事", "近 10 万场", "群众参与度高")

st.divider()

st.subheader("📋 本平台服务数据看板（系统仿真数据）")
# 读取所有交互数据，算一下系统办了多少事
try:
    df_inter = pd.read_csv("data/simulated_interactions.csv", encoding='gbk')
    matched_count = df_inter['matched'].sum()
    
    c1, c2 = st.columns(2)
    c1.metric("累计完成智能匹配人次", f"{matched_count} 人次")
    c2.metric("系统服务赛事数量", "15 场")
    
    st.info("决策建议：基于系统匹配热度，建议2027年在西安、咸阳等核心城市，增加“路跑”和“健步”类赛事的配额，以缓解供需不平衡问题。")
except Exception as e:
    st.error(f"系统数据读取失败: {e}")