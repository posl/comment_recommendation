def main():
    # 读取输入
    s = input()
    # 计算并输出答案
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - week.index(s))
