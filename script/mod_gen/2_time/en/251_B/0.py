def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[i] + A[j] + A[k] <= W:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()