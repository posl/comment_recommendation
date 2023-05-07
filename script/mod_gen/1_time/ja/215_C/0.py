def main():
    import itertools
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    for i, p in enumerate(itertools.permutations(S)):
        if i == K - 1:
            print(''.join(p))
            break

if __name__ == '__main__':
    main()