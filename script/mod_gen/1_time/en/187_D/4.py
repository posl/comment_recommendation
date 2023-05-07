def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))
        B.append((b, a))
    A.sort(reverse=True)
    B.sort(reverse=True)
    aoki = 0
    takahashi = 0
    for i in range(N):
        aoki += A[i][0]
        takahashi += B[i][0]
        if aoki < takahashi:
            print(i+1)
            return

if __name__ == '__main__':
    main()