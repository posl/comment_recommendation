def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = []
    for s in S:
        ans.append(s)
        ans.append('_')
    ans.pop()
    ans = ''.join(ans)
    if ans in T:
        print(-1)
    else:
        print(ans)
