def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max = A[-1]
    B = [0] * (max + 1)
    for i in range(N):
        for j in range(A[i], max + 1, A[i]):
            B[j] += 1
    ans = 0
    for i in range(max + 1):
        ans += B[i] * i
    print(ans)

if __name__ == '__main__':
    main()