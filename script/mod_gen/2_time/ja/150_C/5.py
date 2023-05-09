def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    import itertools
    X = list(itertools.permutations(range(1,N+1)))
    print(abs(X.index(tuple(P)) - X.index(tuple(Q))))

if __name__ == '__main__':
    main()