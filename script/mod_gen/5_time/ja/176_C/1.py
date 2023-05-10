def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            print(-1)
            return
        elif A[i] < i + 1:
            ans += i + 1 - A[i]
    print(ans)

if __name__ == '__main__':
    main()