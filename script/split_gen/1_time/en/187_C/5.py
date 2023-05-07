def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = [s[1:] for s in S if s.startswith("!")]
    S2 = [s for s in S if not s.startswith("!")]
    S1 = set(S1)
    S2 = set(S2)
    for s in S1:
        if s in S2:
            print(s)
            return
    print("satisfiable")
