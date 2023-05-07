def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == "!":
            S1.add(s)
        else:
            S2.add(s)
    for s in S1:
        if s[1:] in S2:
            print(s[1:])
            return
    print("satisfiable")
