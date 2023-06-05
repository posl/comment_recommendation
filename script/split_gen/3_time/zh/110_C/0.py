def main():
    s = input()
    t = input()
    if len(s) != len(t):
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
    for i in s_dict:
        if i not in t_dict or s_dict[i] != t_dict[i]:
            print('No')
            return
    print('Yes')
