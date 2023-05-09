def main():
    N = int(input())
    N_list = list(map(int, list(str(N))))
    S_N = sum(N_list)
    if N % S_N == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()