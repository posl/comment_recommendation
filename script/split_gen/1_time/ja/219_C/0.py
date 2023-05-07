def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    for s in S:
        print(s)
