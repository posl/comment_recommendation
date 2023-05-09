def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = list(set(permutations(S)))
    S.sort()
    print("".join(S[K-1]))
