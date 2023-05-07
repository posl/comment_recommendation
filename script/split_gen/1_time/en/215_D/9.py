def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    G = [0] * (M + 1)
    for i in range(M + 1):
        for j in range(i, M + 1, i):
            G[j] += 1
    ans = [0] * (M + 1)
    for a in A:
        ans[a] = 1
    for i in range(2, M + 1):
        if ans[i] == 0 and G[i] == 2:
            for j in range(i, M + 1, i):
                ans[j] = 1
    print(sum(ans))
    for i in range(1, M + 1):
        if ans[i] == 0:
            print(i)
main()
