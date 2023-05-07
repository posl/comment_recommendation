def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == "!":
            S1.add(s[1:])
        else:
            S2.add(s)
    ans = S1 & S2
    if ans:
        print(list(ans)[0])
    else:
        print("satisfiable")
main()

if __name__ == '__main__':
    main()