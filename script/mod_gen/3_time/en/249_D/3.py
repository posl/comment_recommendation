def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] == A[j]:
                continue
            if A[i] == 1:
                ans += N - j - 1
                continue
            for k in range(j+1, N):
                if A[i] == A[k]:
                    continue
                if A[j] == A[k]:
                    continue
                if A[i] * A[j] == A[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()