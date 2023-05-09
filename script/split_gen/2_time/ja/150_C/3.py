def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = [int(i) for i in input().split()]
    perm = [i for i in range(1, N+1)]
    P_index = 0
    Q_index = 0
    for i, p in enumerate(permutations(perm)):
        if list(p) == P:
            P_index = i
        if list(p) == Q:
            Q_index = i
    print(abs(P_index - Q_index))
