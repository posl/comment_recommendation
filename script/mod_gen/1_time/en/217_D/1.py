def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        elif c == 2:
            cuts.sort()
            for j in range(len(cuts)):
                if cuts[j] == x:
                    print(cuts[j + 1] - cuts[j])
                    break

if __name__ == '__main__':
    main()