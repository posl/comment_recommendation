def main():
    # 获取输入内容
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 求解
    ans = 0
    for i in range(10):
        for j in range(n):
            if s[j][i] == str(i):
                ans += 1
                break
    print(ans)
