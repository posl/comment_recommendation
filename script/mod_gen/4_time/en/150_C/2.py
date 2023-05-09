def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    from itertools import permutations
    perms = list(permutations(range(1, N+1)))
    print(abs(perms.index(tuple(P)) - perms.index(tuple(Q))))

if __name__ == '__main__':
    main()