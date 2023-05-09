def main():
    N = int(input())
    S = [input() for i in range(N)]
    print('Yes' if S.count('For') > (N // 2) else 'No')

if __name__ == '__main__':
    main()