def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                if A[i] * A[k] == A[j] * A[j]:
                    ans += 1
    print(ans // 2)

if __name__ == '__main__':
    main()