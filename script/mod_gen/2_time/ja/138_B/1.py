def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += 1/a
    print(1/ans)

if __name__ == '__main__':
    main()