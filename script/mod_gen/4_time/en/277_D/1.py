def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for i in range(N):
        B[A[i]] += 1
    for i in range(M):
        if B[i] > 0:
            for j in range(M):
                if B[(i+j)%M] > 0:
                    B[(i+j)%M] -= 1
                    break
    ans = 0
    for i in range(M):
        ans += i * B[i]
    print(ans)
main()

if __name__ == '__main__':
    main()