def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aの要素の種類数をカウント
    kind = len(set(A))
    #Aの要素の種類数をカウントするための辞書
    d = {}
    for i in range(N):
        d[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d2 = {}
    for i in range(N):
        d2[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d2[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d3 = {}
    for i in range(N):
        d3[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d3[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d4 = {}
    for i in range(N):
        d4[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d4[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d5 = {}
    for i in range(N):
        d5[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d5[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d6 = {}
    for i in range(N):
        d6[A[i]] = 0
    #A
