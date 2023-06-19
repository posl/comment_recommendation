def main():
    N = input()
    N_len = len(N)
    N_int = int(N)
    N_int_list = [int(i) for i in N]
    N_int_list.sort(reverse=True)
    #print(N_int_list)
    sum_N = sum(N_int_list)
    #print(sum_N)
    if sum_N%3 == 0:
        print(0)
    else:
        if N_int%3 == 0:
            print(0)
        else:
            if N_int%3 == 1:
                if 1 in N_int_list:
                    print(1)
                elif 4 in N_int_list:
                    print(1)
                elif 7 in N_int_list:
                    print(1)
                else:
                    print(-1)
            else:
                if 2 in N_int_list:
                    print(1)
                elif 5 in N_int_list:
                    print(1)
                elif 8 in N_int_list:
                    print(1)
                else:
                    print(-1)
