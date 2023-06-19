def main():
    # 读取输入
    week = input().strip()
    # 处理
    week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    week_index = week_list.index(week)
    day = 7 - week_index
    # 输出
    print(day)
