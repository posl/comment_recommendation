def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    for i in range(N):
        ans += (i + 1) * A[i] - B[i]
    print(ans)
    return

if __name__ == '__main__':
    main()