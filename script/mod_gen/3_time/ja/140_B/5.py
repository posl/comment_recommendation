def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i != N - 1 and A[i] + 1 == A[i + 1]:
            ans += C[A[i] - 1]
    print(ans)

if __name__ == '__main__':
    main()