def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    A = [a for a in A if a <= 0]
    B = [a for a in A if a > 0]
    C = [a for a in A if a == 0]
    D = [a for a in B if a == 0]
    E = [a for a in B if a > 0]
    if len(C) > 0:
        if len(C) * (N - len(C)) >= K:
            print(0)
            return
        K -= len(C) * (N - len(C))
    if len(D) > 0:
        if len(D) * (N - len(D)) >= K:
            print(0)
            return
        K -= len(D) * (N - len(D))
    if len(A) == 0 or len(E) == 0:
        print(E[-1] * E[-2])
        return
    ans = []
    for a in A:
        for e in E:
            ans.append(a * e)
    ans = sorted(ans)
    print(ans[K - 1])

if __name__ == '__main__':
    main()