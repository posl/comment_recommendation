def main():
    N = int(input())
    d = {}
    for i in range(N):
        S, P = input().split()
        P = int(P)
        if S in d:
            d[S].append((P, i+1))
        else:
            d[S] = [(P, i+1)]
    for k, v in sorted(d.items()):
        for p, i in sorted(v, reverse=True):
            print(i)

if __name__ == '__main__':
    main()