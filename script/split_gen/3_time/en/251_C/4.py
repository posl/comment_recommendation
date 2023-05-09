def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    s_set = set(s)
    s_list = list(s_set)
    s_list.sort()
    s_dict = {}
    for i in range(len(s_list)):
        s_dict[s_list[i]] = i
    t_list = [0] * len(s_list)
    for i in range(n):
        t_list[s_dict[s[i]]] = max(t_list[s_dict[s[i]]], t[i])
    t_list.sort()
    print(t_list[-1])
