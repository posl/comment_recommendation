def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(int(ti))
    max_t = max(t)
    max_t_index = t.index(max_t)
    s_max_t = s[max_t_index]
    s_max_t_index = s.index(s_max_t)
    s_max_t_list = []
    for i in range(n):
        if s[i] == s_max_t:
            s_max_t_list.append(i)
    if len(s_max_t_list) == 1:
        print(s_max_t_index + 1)
    else:
        print(min(s_max_t_list) + 1)
