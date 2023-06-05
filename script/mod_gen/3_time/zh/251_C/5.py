def main():
    # 读取输入
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_t = input().split()
        s.append(s_t[0])
        t.append(int(s_t[1]))
    # print(s)
    # print(t)
    # 处理输入
    s_t = {}
    for i in range(n):
        if s_t.get(s[i]) == None:
            s_t[s[i]] = t[i]
        else:
            s_t[s[i]] = max(s_t[s[i]], t[i])
    # print(s_t)
    # 处理输出
    max_t = 0
    max_s = ''
    for i in range(n):
        if max_t < s_t[s[i]]:
            max_t = s_t[s[i]]
            max_s = s[i]
    # print(max_t)
    # print(max_s)
    for i in range(n):
        if max_s == s[i] and max_t == t[i]:
            print(i + 1)
            break
main()
