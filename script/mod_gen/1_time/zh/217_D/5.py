def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx]-cuts[idx-1])

if __name__ == '__main__':
    main()