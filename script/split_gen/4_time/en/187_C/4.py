def main():
    N = int(input())
    S = [input() for _ in range(N)]
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
    return
