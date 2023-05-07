def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    from itertools import permutations
    for i, p in enumerate(permutations(range(1, N+1)), 1):
        if list(p) == P:
            a = i
        if list(p) == Q:
            b = i
    print(abs(a-b))

if __name__ == '__main__':
    main()