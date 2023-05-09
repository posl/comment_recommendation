def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [i for i in a if i != x]
    print(*ans)

if __name__ == '__main__':
    main()