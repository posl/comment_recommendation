def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    sortS = sorted(S, key=lambda x: [X.index(c) for c in x])
    print(*sortS, sep='
')
