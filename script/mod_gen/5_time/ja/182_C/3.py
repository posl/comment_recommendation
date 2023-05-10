def main():
    N = input()
    N_len = len(N)
    if N_len == 1:
        if N == "0":
            print(0)
            return
        elif N == "3" or N == "6" or N == "9":
            print(0)
            return
        else:
            print(-1)
            return
    elif N_len == 2:
        if int(N) % 3 == 0:
            print(0)
            return
        elif N[0] == "0":
            print(1)
            return
        elif N[1] == "0":
            print(1)
            return
        else:
            print(-1)
            return
    else:
        N_list = list(N)
        N_list = [int(n) for n in N_list]
        N_list.sort()
        N_sum = sum(N_list)
        if N_sum % 3 == 0:
            print(0)
            return
        elif N_sum % 3 == 1:
            if 1 in N_list:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(1)
                    return
            elif 4 in N_list:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(1)
                    return
            elif 7 in N_list:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(1)
                    return
            else:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(2)
                    return
        else:
            if 2 in N_list:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(1)
                    return
            elif 5 in N_list:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(1)
                    return
            elif 8 in N_list:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(1)
                    return
            else:
                if N_len == 3:
                    print(-1)
                    return
                else:
                    print(2)
                    return

if __name__ == '__main__':
    main()