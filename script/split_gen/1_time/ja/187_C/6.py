def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    for i in S:
        if "!" + i in S:
            print(i)
            exit()
    print("satisfiable")
