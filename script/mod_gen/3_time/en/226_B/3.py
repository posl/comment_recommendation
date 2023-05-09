def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    ans = 1
    prev = A[0]
    for i in range(1, N):
        if prev != A[i]:
            ans += 1
            prev = A[i]
    print(ans)

if __name__ == '__main__':
    main()