def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    s_t = {}
    for i in range(n):
        if s[i] in s_t:
            s_t[s[i]].append((i, t[i]))
        else:
            s_t[s[i]] = [(i, t[i])]
    for key in s_t:
        s_t[key].sort(key=lambda x: x[1], reverse=True)
    s_t = sorted(s_t.items(), key=lambda x: x[1][0][1], reverse=True)
    print(s_t[0][1][0][0] + 1)
