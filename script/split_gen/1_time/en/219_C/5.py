def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    new_order = {c: i for i, c in enumerate(X)}
    S.sort(key=lambda s: [new_order[c] for c in s])
    print(*S, sep='
')
