def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    if s == t:
        print('Yes')
        return
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print('No')
        return
    s_set = set(s_list)
    t_set = set(t_list)
    if len(s_set) != len(t_set):
        print('No')
        return
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]].append(i)
        else:
            s_dict[s[i]] = [i]
        if t[i] in t_dict:
            t_dict[t[i]].append(i)
        else:
            t_dict[t[i]] = [i]
    for key in s_dict:
        if s_dict[key] != t_dict[key]:
            print('No')
            return
    print('Yes')
    return
