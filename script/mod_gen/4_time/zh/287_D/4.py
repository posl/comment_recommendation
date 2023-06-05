def solve(s, t):
    s_list = list(s)
    t_list = list(t)
    for i in range(len(t)):
        if s_list[i] != '?' and s_list[i] != t_list[i]:
            return 'No'
        s_list[i] = t_list[i]
    if s_list.count('?') == 0:
        return 'Yes'
    for i in range(len(t), len(s)):
        if s_list[i] == '?':
            s_list[i] = 'a'
    return 'Yes'

if __name__ == '__main__':
    solve()