def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        if s[i] not in s_map:
            s_map[s[i]] = 1
        else:
            s_map[s[i]] += 1
        if t[i] not in t_map:
            t_map[t[i]] = 1
        else:
            t_map[t[i]] += 1
    if s_map == t_map:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()