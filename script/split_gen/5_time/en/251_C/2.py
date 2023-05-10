def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = t[i]
        else:
            if d[s[i]] < t[i]:
                d[s[i]] = t[i]
    max_t = 0
    for i in d:
        if d[i] > max_t:
            max_t = d[i]
    for i in range(n):
        if t[i] == max_t:
            print(i + 1)
            break
