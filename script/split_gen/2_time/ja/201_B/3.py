def main():
    #入力
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    
    #ソート
    T_sort = sorted(T, reverse=True)
    
    #出力
    print(S[T.index(T_sort[1])])
