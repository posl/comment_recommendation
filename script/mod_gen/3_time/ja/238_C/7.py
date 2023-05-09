def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_first = int(N_str[0])
    N_last = int(N_str[-1])
    N_mid = int(N_str[1:-1]) if N_len > 2 else 0
    #print(N, N_len, N_first, N_mid, N_last)
    if N_len == 1:
        print(N)
    elif N_len == 2:
        print(N_first + (N_last - 1) * 2)
    else:
        print(N_first + (N_mid - 1) * 2 + 9 * (N_len - 2) * (N_mid + 1) + N_last)

if __name__ == '__main__':
    main()