def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = set()
        s_dict[s[i]].add(i)
        if t[i] not in t_dict:
            t_dict[t[i]] = set()
        t_dict[t[i]].add(i)
    s_set = set(s)
    t_set = set(t)
    if s_set != t_set:
        print("No")
        return
    for i in s_set:
        if s_dict[i] != t_dict[i]:
            print("No")
            return
    print("Yes")
    return
