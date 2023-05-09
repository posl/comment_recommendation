def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    N, X = map(int, input().split())
    A = []
    for _ in range(N):
        L, *A_ = map(int, input().split())
        A.append(A_)
    A = [a for a in A if X in a]
    N = len(A)
    if N == 0:
        print(0)
        return
    C = Counter()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for a in A[i]:
                for b in A[j]:
                    C[a*b] += 1
    ans = 0
    for a in A[0]:
        if X % a == 0 and X // a in C:
            ans += C[X//a]
    print(ans)
