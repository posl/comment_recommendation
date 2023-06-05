def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len >= t_len:
        print("No")
        return
    else:
        t_index = 0
        for s_index in range(s_len):
            if s[s_index] == t[t_index]:
                t_index += 1
            else:
                if s_index == 0:
                    print("No")
                    return
        print("Yes")
        return
