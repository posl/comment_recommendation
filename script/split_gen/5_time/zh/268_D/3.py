def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    # 逆向思维，先构造出满足条件的字符串，再检查是否与给定字符串冲突
    # 从最后一个字符串开始构造，检查是否与给定字符串冲突
    # 与给定字符串冲突的话，将该字符串的下一个字符串放到当前字符串的后面，再次检查是否冲突
    # 重复上述操作，直到不冲突为止
    # 从最后一个字符串开始构造
    ans = s[-1]
    # 从倒数第二个字符串开始，直到第一个字符串
    for i in range(n-2, -1, -1):
        # 检查是否与给定字符串冲突
        if ans.startswith(s[i]) or ans.endswith(s[i]):
            # 将该字符串的下一个字符串放到当前字符串的后面
            ans = s[i] + ans
        else:
            # 将该字符串放到当前字符串的前面
            ans = ans + s[i]
    # 检查是否与给定字符串冲突
    for i in range(m):
        if ans == t[i]:
            print(-1)
            return
    print(ans)
