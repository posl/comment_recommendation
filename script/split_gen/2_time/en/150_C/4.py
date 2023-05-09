def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    from itertools import permutations
    perm = list(permutations(range(1,N+1)))
    print(abs(perm.index(tuple(P))-perm.index(tuple(Q))))
