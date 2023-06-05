def solve():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if s[0] == "!":
            if s[1:] in S:
                print(s[1:])
                return
        else:
            if "!" + s in S:
                print(s)
                return
    print("satisfiable")

if __name__ == '__main__':
    solve()