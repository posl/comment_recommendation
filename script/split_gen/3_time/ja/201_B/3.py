def main():
    #入力
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #問題文の通りに処理
    T.sort(reverse=True)
    print(S[T.index(T[1])])
