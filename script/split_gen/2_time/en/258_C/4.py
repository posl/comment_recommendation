def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for t, x in queries:
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            ans.append(S[x-1])
    print(''.join(ans))
