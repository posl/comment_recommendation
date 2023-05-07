def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    d = {c:i for i, c in enumerate(X)}
    S.sort(key=lambda s:[d[c] for c in s])
    for s in S:
        print(s)
