def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s.count('For') > n // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()