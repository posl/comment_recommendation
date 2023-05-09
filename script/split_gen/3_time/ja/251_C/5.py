def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #print(S)
    #print(T)
    #print(S)
    #print(T)
    #最も得点が高い提出を求める
    S_T = []
    for i in range(N):
        S_T.append([S[i], T[i]])
    #print(S_T)
    #得点が高い順にソート
    S_T.sort(key = lambda x:x[1], reverse = True)
    #print(S_T)
    #print(S_T)
    #ソート後のリストを作成
    S_sort = []
    T_sort = []
    for i in range(N):
        S_sort.append(S_T[i][0])
        T_sort.append(S_T[i][1])
    #print(S_sort)
    #print(T_sort)
    #print(S_sort)
    #print(T_sort)
    #ソート後のリストから最も得点が高い提出を求める
    S_T_sort = []
    for i in range(N):
        S_T_sort.append([S_sort[i], T_sort[i]])
    #print(S_T_sort)
    #print(S_T_sort)
    #最も得点が高い提出を求める
    max_T = T_sort[0]
    #print(max_T)
    #最も得点が高い提出のインデックスを求める
    max_T_index = T.index(max_T)
    #print(max_T_index)
    #最も得点が高い提出のインデックスをもとに元のリストから最も得点が高い提出の文字列を求める
    max_S = S[max_T_index]
    #print(max_S)
    #最も得点が高い提出の文字列をもとに元のリストから最も得点が高い提出のインデックスを求める
    max_S_index = S.index(max_S)
    #print(max_S_index)
    #最も得点が高い提出のインデックスをもとに元のリストから最
