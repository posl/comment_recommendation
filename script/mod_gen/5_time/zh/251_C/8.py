def problems251_c():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        ss,tt = input().split()
        s.append(ss)
        t.append(int(tt))
    m = {}
    for i in range(n):
        if s[i] not in m:
            m[s[i]] = t[i]
    max_num = -1
    max_index = -1
    for i in range(n):
        if s[i] in m and m[s[i]] > max_num:
            max_num = m[s[i]]
            max_index = i
    print(max_index+1)

if __name__ == '__main__':
    problems251_c()