def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S2 = []
    for s in S:
        if s in S2:
            S2.append(s+"("+str(S2.count(s))+")")
        else:
            S2.append(s)
    print(*S2, sep='
')

if __name__ == '__main__':
    main()