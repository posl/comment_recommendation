def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    # 用于存储字母的位置
    s_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = [i]
        else:
            s_dict[s[i]].append(i)
    # print(s_dict)
    # 用于存储字母的位置
    t_dict = {}
    for i in range(len(t)):
        if t[i] not in t_dict:
            t_dict[t[i]] = [i]
        else:
            t_dict[t[i]].append(i)
    # print(t_dict)
    # 用于存储不同字母的位置
    diff = []
    for i in range(len(s)):
        if s[i] != t[i]:
            diff.append(i)
    # print(diff)
    # 用于记录不同字母的位置是否相同
    flag = True
    for i in diff:
        if s[i] not in t_dict or t[i] not in s_dict:
            flag = False
            break
        elif s_dict[s[i]] != t_dict[t[i]]:
            flag = False
            break
    if flag:
        print(1)
    else:
        print(2)
