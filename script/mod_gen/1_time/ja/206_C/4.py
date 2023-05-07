def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N = int(readline())
    A = list(map(int,readline().split()))
    if len(A) != N:
        print("入力エラー")
        return
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += N - i - 1 - (A[i] == A[i+1])
    print(ans)

if __name__ == '__main__':
    main()