def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if s.count('For') > n // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()