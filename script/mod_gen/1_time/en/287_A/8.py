def main():
    # input
    n = int(input())
    s = [input() for _ in range(n)]
    # compute
    majority = s.count('For') > n/2
    # output
    print('Yes' if majority else 'No')

if __name__ == '__main__':
    main()