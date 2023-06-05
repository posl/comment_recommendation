def main():
    n = int(input())
    s = [input() for i in range(n)]
    if s.count('For') > s.count('Against'):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()