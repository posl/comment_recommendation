def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    s_dic = {}
    t_dic = {}
    for i in range(len(s)):
        if s[i] not in s_dic:
            s_dic[s[i]] = t[i]
        else:
            if s_dic[s[i]] != t[i]:
                print("No")
                return
        if t[i] not in t_dic:
            t_dic[t[i]] = s[i]
        else:
            if t_dic[t[i]] != s[i]:
                print("No")
                return
    print("Yes")
    return
