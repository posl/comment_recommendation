def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += a - 1
    print(ans)

if __name__ == '__main__':
    main()