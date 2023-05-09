def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    t_list = list(t)
    s_list = list(s)
    for i in range(s_len - t_len + 1):
        for j in range(t_len):
            if s_list[i + j] != t_list[j] and s_list[i + j] != "?":
                break
            if j == t_len - 1:
                for k in range(t_len):
                    s_list[i + k] = t_list[k]
                for k in range(s_len):
                    if s_list[k] == "?":
                        s_list[k] = "a"
                for k in range(s_len):
                    print(s_list[k], end="")
                print()
                return
    print("UNRESTORABLE")

if __name__ == '__main__':
    main()