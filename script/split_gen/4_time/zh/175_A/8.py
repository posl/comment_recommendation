def main():
    # 读入数据
    s = input()
    # 计算答案
    ans = 0
    for i in range(3):
        if s[i] == "R":
            ans += 1
    # 输出答案
    print(ans)
