def main():
    # 读入数据
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 处理数据
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(n):
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
        elif s[i] == "TLE":
            tle += 1
        elif s[i] == "RE":
            re += 1
    # 输出结果
    print("AC x", ac)
    print("WA x", wa)
    print("TLE x", tle)
    print("RE x", re)
