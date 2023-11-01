def main():
    import sys
    import datetime
    # 读取输入
    s = sys.stdin.readline().strip()
    # 计算
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    i = week.index(s)
    # 统计天数
    days = 0
    for j in range(i, 7):
        if week[j] == 'Saturday':
            break
        days += 1
    # 输出
    print(days)
