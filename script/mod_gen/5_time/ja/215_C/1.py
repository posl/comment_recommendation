def main():
    import sys
    input = sys.stdin.readline
    from itertools import permutations
    S, K = input().rstrip().split()
    K = int(K)
    S = sorted(S)
    S = ''.join(S)
    S = list(set(permutations(S)))
    S.sort()
    S = [''.join(s) for s in S]
    print(S[K-1])
main()

if __name__ == '__main__':
    main()