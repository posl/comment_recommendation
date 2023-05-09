def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input().strip()
    win = {'r':P,'s':R,'p':S}
    ans = 0
    for i in range(N):
        if i < K:
            ans += win[T[i]]
        else:
            if T[i] == T[i-K]:
                if i+K < N and T[i] != T[i+K]:
                    ans += win[T[i]]
                    T = T[:i] + 'x' + T[i+1:]
            else:
                ans += win[T[i]]
    print(ans)
