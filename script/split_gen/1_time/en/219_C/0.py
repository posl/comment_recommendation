def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    print('
'.join(sorted(S, key=lambda s: [X.index(c) for c in s])))
