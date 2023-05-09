def main():
    import sys
    readline = sys.stdin.readline
    N = int(readline())
    S = list(map(int, readline().split()))
    T = list(map(int, readline().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        if ans[i] > ans[(i+1)%N]:
            ans[(i+1)%N] = ans[i] + S[i]
    for i in range(N-1, -1, -1):
        if ans[i] > ans[(i+1)%N]:
            ans[(i+1)%N] = ans[i] + S[i]
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()