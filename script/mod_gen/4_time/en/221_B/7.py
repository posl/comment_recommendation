def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list) - 1):
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
        if s_list == t_list:
            print("Yes")
            return
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
    print("No")

if __name__ == '__main__':
    main()