def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[-1] < sum(s[:-1]):
        print(0)
    else:
        print(s[-1] - sum(s[:-1]))

if __name__ == '__main__':
    main()