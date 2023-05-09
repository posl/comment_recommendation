def problems251_c():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_t = input().split()
        s.append(s_t[0])
        t.append(int(s_t[1]))
    max_t = max(t)
    max_s = []
    for i in range(n):
        if t[i] == max_t:
            max_s.append(s[i])
    max_s.sort()
    print(s.index(max_s[0])+1)
    return

if __name__ == '__main__':
    problems251_c()