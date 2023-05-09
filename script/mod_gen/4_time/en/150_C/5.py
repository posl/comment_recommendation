def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    from itertools import permutations
    P = list(permutations(P))
    Q = list(permutations(Q))
    P.sort()
    Q.sort()
    print(abs(P.index(tuple(P)) - Q.index(tuple(Q))))

if __name__ == '__main__':
    main()