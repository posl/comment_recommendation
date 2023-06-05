def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        print("No")
        return
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return
    s_dict = {}
    t_dict = {}
    for i in range(s_len):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    s_list = list(s_dict.values())
    t_list = list(t_dict.values())
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return
    print("Yes")
