def main():
    s = input()
    t = input()
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
    if sorted(s_dict.values()) == sorted(t_dict.values()):
        print("Yes")
    else:
        print("No")
