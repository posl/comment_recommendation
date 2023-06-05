def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    # 用一个字典记录S中每个字母出现的位置
    s_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = [i]
        else:
            s_dict[s[i]].append(i)
    # 用一个字典记录T中每个字母出现的位置
    t_dict = {}
    for i in range(len(t)):
        if t[i] not in t_dict:
            t_dict[t[i]] = [i]
        else:
            t_dict[t[i]].append(i)
    # 如果s和t中有不同的字母，返回No
    if len(s_dict) != len(t_dict):
        print("No")
        return
    # 如果s和t中有相同的字母，但是出现的次数不同，返回No
    for key in s_dict:
        if key not in t_dict:
            print("No")
            return
        if len(s_dict[key]) != len(t_dict[key]):
            print("No")
            return
    # 如果s和t中有相同的字母，出现的次数也相同，但是出现的位置不同，返回No
    for key in s_dict:
        for i in range(len(s_dict[key])):
            if s_dict[key][i] != t_dict[key][i]:
                print("No")
                return
    print("Yes")
    return
