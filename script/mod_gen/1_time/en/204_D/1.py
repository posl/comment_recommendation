def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i] * (N - i)
    print(ans)

if __name__ == '__main__':
    main()