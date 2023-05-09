def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    print('
'.join(S))
