def main():
    from itertools import permutations
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for p in permutations(s):
        x = '_'.join(p)
        if 3 <= len(x) <= 16 and not any(x in t for t in t):
            print(x)
            return
    print(-1)

if __name__ == '__main__':
    main()