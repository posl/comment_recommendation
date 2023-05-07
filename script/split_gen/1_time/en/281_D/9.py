def main():
    # read input
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # solve problem
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        S.update([sum(A[:i+1])])
    # write output
    for i in range(max(S), -1, -1):
        if i % D == 0:
            print(i)
            return
    print(-1)
