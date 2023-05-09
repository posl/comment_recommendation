def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] % 200
    C = [0] * 200
    for i in range(N):
        C[B[i]] += 1
    ans = 0
    for i in range(200):
        ans += C[i] * (C[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()