def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                if A[i] * A[k] == A[j]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()