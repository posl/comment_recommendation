def main():
    N = int(input())
    lst = [input() for i in range(N)]
    if lst.count('For') > N // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()