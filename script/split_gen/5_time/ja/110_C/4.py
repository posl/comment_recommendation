def main():
    s = input()
    t = input()
    s_dic = {}
    t_dic = {}
    for i in range(len(s)):
        if s[i] in s_dic:
            s_dic[s[i]].append(i)
        else:
            s_dic[s[i]] = [i]
        if t[i] in t_dic:
            t_dic[t[i]].append(i)
        else:
            t_dic[t[i]] = [i]
    s_list = sorted(s_dic.items(), key=lambda x:x[1])
    t_list = sorted(t_dic.items(), key=lambda x:x[1])
    for i in range(len(s_list)):
        if s_list[i][1] != t_list[i][1]:
            print('No')
            exit()
    print('Yes')
