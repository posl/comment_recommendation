def main():
    # data load
    s = input()
    q = int(input())
    # print(s)
    # print(q)
    # print(q_list)
    # print(f_list)
    # print(c_list)
    # print(t_list)
    # main
    reverse_count = 0
    reverse_flag = False
    front_flag = True
    s_list = list(s)
    for i in range(q):
        q_list = input().split()
        # print(q_list)
        if q_list[0] == "1":
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        elif q_list[0] == "2":
            if q_list[1] == "1":
                if reverse_flag:
                    s_list.append(q_list[2])
                else:
                    s_list.insert(0, q_list[2])
            elif q_list[1] == "2":
                if reverse_flag:
                    s_list.insert(0, q_list[2])
                else:
                    s_list.append(q_list[2])
        # print(s_list)
    if reverse_flag:
        s_list.reverse()
    print("".join(s_list))

if __name__ == '__main__':
    main()