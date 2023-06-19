def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(0, t_len + 1):
        s_new = s[0:i] + t_len * "?" + s[i + t_len:s_len]
        flag = True
        for j in range(0, s_len):
            if s_new[j] == "?":
                continue
            elif s_new[j] == t[j]:
                continue
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")
