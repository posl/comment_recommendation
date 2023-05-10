def main():
    N = input()
    N_len = len(N)
    N_int = int(N)
    N_list = [int(i) for i in N]
    if N_len == 2:
        print(N_list[0] * N_list[1])
        return
    if N_len == 3:
        print(N_list[0] * N_list[1] * N_list[2])
        return
    if N_len == 4:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3])
        return
    if N_len == 5:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4])
        return
    if N_len == 6:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5])
        return
    if N_len == 7:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6])
        return
    if N_len == 8:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6] * N_list[7])
        return
    if N_len == 9:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6] * N_list[7] * N_list[8])
        return
    if N_len == 10:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6] * N_list[7] * N_list[8] * N_list[9])
        return

if __name__ == '__main__':
    main()