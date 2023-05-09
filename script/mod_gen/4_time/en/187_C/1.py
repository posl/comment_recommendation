def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = set()
    for s in S:
        if s[0] == "!":
            T.add(s[1:])
        else:
            T.add(s)
    for t in T:
        if "!" + t in T:
            print(t)
            return
    print("satisfiable")
    return

if __name__ == '__main__':
    main()