def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        ans = (B[N // 2] - A[N // 2] + 1) + (B[N // 2 - 1] - A[N // 2 - 1] + 1) - 1
    else:
        ans = B[N // 2] - A[N // 2] + 1
    print(ans)

if __name__ == '__main__':
    main()