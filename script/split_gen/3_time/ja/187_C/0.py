def main():
    N = int(input())
    S = [input() for i in range(N)]
    S1 = [s[1:] for s in S if s[0] == "!"]
    S2 = [s for s in S if s[0] != "!"]
    S1.sort()
    S2.sort()
    for i in range(N-1):
        if S1[i] == S2[i]:
            print(S1[i])
            return
    print("satisfiable")
