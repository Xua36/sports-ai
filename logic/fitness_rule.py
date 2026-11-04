def assess_fitness(age, resting_hr, fitness_level):
    """
    身体状况动态评估规则：
    根据年龄、静息心率和体能自评，给出能力等级和风险提示
    """
    # 基础等级由自评决定（1-5分）
    base_level = fitness_level
    
    # 风险提示逻辑
    risk = "正常"
    if resting_hr > 85 or (age > 50 and fitness_level <= 2):
        risk = "较高（建议赛前体检）"
    elif resting_hr > 75 or (age > 40 and fitness_level <= 2):
        risk = "中等（注意循序渐进）"
        
    # 推荐赛事强度（1-5级）
    # 算法：综合体能和年龄做一个简单扣减
    recommend_intensity = base_level
    if age > 45: recommend_intensity -= 1
    if resting_hr > 80: recommend_intensity -= 1
    
    recommend_intensity = max(1, min(5, recommend_intensity)) # 限制在1-5之间
    
    # 置信度（如果是极端数据，置信度降低）
    confidence = "高"
    if age > 60 or resting_hr > 90:
        confidence = "中（建议结合线下实测）"

    return {
        "level": base_level,
        "recommend_intensity": recommend_intensity,
        "risk": risk,
        "confidence": confidence
    }
def recovery_assess(load_level, fatigue_score):
    """
    赛后恢复评估规则：
    根据运动负荷和疲劳度，给出恢复时间建议
    """
    if fatigue_score >= 8 or load_level >= 5:
        return {"time": "72小时以上", "advice": "建议完全休息，进行拉伸和理疗，暂停高强度运动。", "status": "warning"}
    elif fatigue_score >= 5 or load_level >= 3:
        return {"time": "24-48小时", "advice": "建议进行低强度活动（如散步、慢跑），保证充足睡眠。", "status": "info"}
    else:
        return {"time": "12-24小时", "advice": "身体状态良好，可进行常规训练，注意补水。", "status": "success"}