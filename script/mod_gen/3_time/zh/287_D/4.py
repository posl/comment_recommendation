def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for x in range(len_t + 1):
        s_new = s[:len_t - x] + s[len_s - x:]
        flag = True
        for i in range(len_t):
            if s_new[i] != t[i] and s_new[i] != '?':
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()