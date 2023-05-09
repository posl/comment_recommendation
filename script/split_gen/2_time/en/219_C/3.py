def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S, key=lambda s: [X.index(c) for c in s])
    print('
'.join(S))
