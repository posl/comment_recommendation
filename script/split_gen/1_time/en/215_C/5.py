def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    import itertools
    s = list(itertools.permutations(S))
    print(''.join(s[K-1]))
