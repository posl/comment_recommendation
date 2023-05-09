def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_half = N_len // 2
    count = 0
    for i in range(1, N+1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len % 2 == 0:
            if i_str[:N_half] == i_str[N_half:]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()