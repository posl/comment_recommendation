def main():
    N = int(input())
    A = []
    B = []
    for i in range(0, N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(0, N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) / 2
    print(int(ans))

if __name__ == '__main__':
    main()