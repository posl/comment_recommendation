def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_list = list(N_str)
    N_list.sort(reverse=True)
    N_list_1 = N_list[0:N_len//2]
    N_list_2 = N_list[N_len//2:N_len]
    N_1 = int("".join(N_list_1))
    N_2 = int("".join(N_list_2))
    print(N_1*N_2)

if __name__ == '__main__':
    main()