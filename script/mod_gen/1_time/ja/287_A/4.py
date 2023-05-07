def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    if l.count('For') > n // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()