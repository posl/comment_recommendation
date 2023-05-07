def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if A[k] == A[i] // A[j]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()