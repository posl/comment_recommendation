def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    print(*p)

if __name__ == '__main__':
    main()