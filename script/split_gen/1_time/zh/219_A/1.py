def get_score_level(score):
    if score >= 0 and score < 40:
        return "新手"
    elif score >= 40 and score < 70:
        return "中级"
    elif score >= 70 and score < 90:
        return "高级"
    elif score >= 90 and score <= 100:
        return "专家"
    else:
        return "输入分数有误"
