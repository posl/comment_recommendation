def main():
    N = int(input())
    D = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] not in D:
            D[L[0]] = [L[1:]]
        else:
            D[L[0]].append(L[1:])
    ans = 1
    for i in D:
        ans *= len(set(map(tuple, D[i])))
        ans %= 10**9 + 7
    print(ans)
