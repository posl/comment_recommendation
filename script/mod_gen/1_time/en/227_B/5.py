def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    if s[-1] > sum(s[:-1]):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()