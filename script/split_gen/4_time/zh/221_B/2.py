def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        s_list = list(S)
        t_list = list(T)
        for i in range(len(s_list)):
            if i == 0:
                s_list[0], s_list[1] = s_list[1], s_list[0]
                if s_list == t_list:
                    print("Yes")
                    break
                else:
                    s_list[0], s_list[1] = s_list[1], s_list[0]
            else:
                s_list[i], s_list[i-1] = s_list[i-1], s_list[i]
                if s_list == t_list:
                    print("Yes")
                    break
                else:
                    s_list[i], s_list[i-1] = s_list[i-1], s_list[i]
        else:
            print("No")
