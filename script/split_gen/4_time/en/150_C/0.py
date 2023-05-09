def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [i - 1 for i in P]
    Q = [i - 1 for i in Q]
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i
    perm = [i for i in range(N)]
    perm = list(itertools.permutations(perm))
    perm.sort()
    perm = [list(i) for i in perm]
    a = perm.index(P)
    b = perm.index(Q)
    print(abs(a - b))
