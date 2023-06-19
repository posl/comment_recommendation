def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[-1] + sum(t[:-1]) // 2)

if __name__ == '__main__':
    main()