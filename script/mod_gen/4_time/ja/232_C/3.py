def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    cd = [tuple(map(int, input().split())) for _ in range(m)]
    ans = 'No'
    for p in permutations(range(n)):
        ok = True
        for a, b in ab:
            if (p.index(a) > p.index(b)) != (a in p[:p.index(b)]):
                ok = False
                break
        for c, d in cd:
            if (p.index(c) > p.index(d)) != (c in p[:p.index(d)]):
                ok = False
                break
        if ok:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()