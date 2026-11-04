import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.ops_cluster import run_user_clustering

st.title("🏢 赛事运营管理端")
st.write("智能体 ⑥：赛事运营决策优化。利用聚类算法分析参赛人群，指导赛事策划与精准营销。")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
user_data_path = os.path.join(BASE_DIR, "data", "simulated_users.csv")

try:
    df_users, group_counts = run_user_clustering(user_data_path)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 用户群体自动聚类")
        st.bar_chart(group_counts)
        
    with col2:
        st.subheader("💡 运营投放建议")
        top_group = group_counts.index[0]
        st.success(f"当前平台**{top_group}**占比最高。")
        if "老年" in top_group:
            st.info("建议：增加社区趣味、健步走赛事的举办频次，加强基础医疗和补给保障。")
        elif "青年" in top_group:
            st.info("建议：重点推广半程马拉松、篮球等中高强度赛事，增加夜间赛或周末赛。")
        else:
            st.info("建议：策划亲子跑、打卡赛等低门槛活动，提升大众参与度。")
            
    st.divider()
    st.subheader("用户聚类明细（部分）")
    st.dataframe(df_users[['user_id', 'age', 'fitness_level', 'group_name']].head(10), use_container_width=True)
    
except Exception as e:
    st.error(f"运营数据分析失败: {e}")