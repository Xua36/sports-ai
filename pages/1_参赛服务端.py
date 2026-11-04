import streamlit as st
import sys
import os
import pandas as pd

# 将根目录加入路径，以便能导入 logic 模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.fitness_rule import assess_fitness, recovery_assess

st.title("👤 参赛服务端")

# 划分三个 Tab 页签，对应三个智能体
tab1, tab2, tab3 = st.tabs(["① 身体状况动态评估", "③ 赛事智能推荐", "⑤ 赛后恢复评估"])

# ================== 智能体 1 ==================
with tab1:
    st.subheader("智能体 ①：身体状况动态评估")
    with st.form("fitness_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("年龄", min_value=10, max_value=90, value=30)
            gender = st.selectbox("性别", ["男", "女"])
        with col2:
            resting_hr = st.number_input("静息心率 (次/分钟)", min_value=40, max_value=120, value=70)
            fitness_level = st.slider("基础体能自评 (1-5分, 5为最强)", 1, 5, 3)
        submit1 = st.form_submit_button("开始评估")
        
    if submit1:
        result = assess_fitness(age, resting_hr, fitness_level)
        st.divider()
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("运动能力等级", f"{result['level']} 级")
        res_col2.metric("推荐赛事强度", f"{result['recommend_intensity']} 级")
        res_col3.metric("评估置信度", result['confidence'])
        if "较高" in result['risk']: st.error(f"⚠️ 风险提示：{result['risk']}")
        elif "中等" in result['risk']: st.warning(f"⚠️ 风险提示：{result['risk']}")
        else: st.info(f"✅ 风险提示：{result['risk']}")

# ================== 智能体 3 ==================
with tab2:
    st.subheader("智能体 ③：赛事—用户双向匹配推荐")
    st.write("基于您的所在城市和项目偏好，为您推荐最匹配的赛事（仿真数据演示）：")
    
    # 读取赛事数据
    try:
        df_events = pd.read_csv("data/simulated_events.csv", encoding='gbk')
        
        col_city, col_sport = st.columns(2)
        with col_city:
            user_city = st.selectbox("您的城市", df_events['city'].unique())
        with col_sport:
            user_sport = st.selectbox("您偏好的项目", df_events['sport_type'].unique())
            
        if st.button("获取推荐赛事"):
            # 简单的标签匹配逻辑
            matched_events = df_events[(df_events['city'] == user_city) & (df_events['sport_type'] == user_sport)]
            
            if len(matched_events) > 0:
                st.success(f"为您找到 {len(matched_events)} 场匹配赛事：")
                st.dataframe(matched_events, use_container_width=True)
            else:
                st.warning("该城市暂时没有您偏好的赛事，为您推荐周边赛事：")
                st.dataframe(df_events[df_events['sport_type'] == user_sport], use_container_width=True)
    except Exception as e:
        st.error(f"赛事数据读取失败：{e}")

# ================== 智能体 5 ==================
with tab3:
    st.subheader("智能体 ⑤：赛后恢复评估")
    st.write("输入您刚完成的赛事情况，获取恢复建议：")
    
    load_level = st.slider("刚刚完成的赛事强度 (1-5级)", 1, 5, 3)
    fatigue_score = st.slider("赛后疲劳感自评 (1-10分, 10为极度疲劳)", 1, 10, 5)
    
    if st.button("生成恢复方案"):
        rec_result = recovery_assess(load_level, fatigue_score)
        st.divider()
        st.metric("建议恢复时间", rec_result["time"])
        
        if rec_result["status"] == "warning":
            st.error(f"**恢复建议：** {rec_result['advice']}")
        elif rec_result["status"] == "info":
            st.info(f"**恢复建议：** {rec_result['advice']}")
        else:
            st.success(f"**恢复建议：** {rec_result['advice']}")