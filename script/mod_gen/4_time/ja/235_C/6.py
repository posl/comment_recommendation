def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        X, K = map(int, input().split())
        ans = 0
        count = 0
        for j in range(N):
            if A[j] == X:
                count += 1
                if count == K:
                    ans = j + 1
                    break
        if ans == 0:
            ans = -1
        print(ans)

if __name__ == '__main__':
    main()