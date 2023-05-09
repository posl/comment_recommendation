def main():
    #入力
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #辞書順にソート
    S.sort(key=lambda x: [X.index(i) for i in x])
    #出力
    for i in range(N):
        print(S[i])
