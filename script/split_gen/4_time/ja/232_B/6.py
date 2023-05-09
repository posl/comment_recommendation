def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len):
        if s == t:
            print("Yes")
            return
        s = s[s_len-1] + s[0:s_len-1]
    print("No")
    return
