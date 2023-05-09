def main():
    import sys
    input = sys.stdin.readline
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # 文字列を辞書順に並べ替える
    X = {X[i]: i for i in range(26)}
    S.sort(key=lambda x: [X[c] for c in x])
    for s in S:
        print(s, end="")

if __name__ == '__main__':
    main()