def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # Xの順番を辞書にしておく
    # X = "zyxwvutsrqponmlkjihgfedcba"
    # X_dict = {"z":0, "y":1, "x":2, ...}
    X_dict = {X[i]:i for i in range(len(X))}
    # Sの文字列をXの順番で並べ替える
    # S = ["a", "ab", "abc", "ac", "b"]
    # S_sort = ["a", "ac", "ab", "abc", "b"]
    S_sort = sorted(S, key=lambda x: [X_dict[s] for s in x])
    # 並べ替えたSを出力
    for s in S_sort:
        print(s)
