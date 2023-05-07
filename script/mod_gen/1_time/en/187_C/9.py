def main():
    N = int(input())
    S = [input() for i in range(N)]
    S1 = set(S)
    S2 = set([s[1:] if s[0] == "!" else "!" + s for s in S])
    if len(S1 & S2) > 0:
        print((S1 & S2).pop())
    else:
        print("satisfiable")

if __name__ == '__main__':
    main()