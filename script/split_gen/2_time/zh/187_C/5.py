def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if "!" + s in S:
            print(s)
            return
    print("satisfiable")
