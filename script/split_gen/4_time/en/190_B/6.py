def main():
    N, S, D = map(int, input().split())
    spells = []
    for _ in range(N):
        X, Y = map(int, input().split())
        spells.append((X, Y))
    for spell in spells:
        if spell[0] < S and spell[1] > D:
            print("Yes")
            return
    print("No")
