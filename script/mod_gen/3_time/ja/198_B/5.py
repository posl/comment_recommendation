def main():
    N = int(input())
    N_str = str(N)
    N_str_rev = N_str[::-1]
    if N_str == N_str_rev:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()