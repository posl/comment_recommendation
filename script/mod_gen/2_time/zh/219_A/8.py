def get_score_level(score):
    if score < 40:
        return "新手"
    elif score < 70:
        return "中级"
    elif score < 90:
        return "高级"
    else:
        return "专家"

if __name__ == '__main__':
    get_score_level()