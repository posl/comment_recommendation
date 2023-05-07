def main():
    N = int(input())
    A = list(map(int, input().split()))
    #Aの各要素の値を、出席番号に変換する
    #0番目は使わない
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] = i+1
    #Bの各要素の値を、Aの各要素の値に変換する
    #0番目は使わない
    C = [0] * (N+1)
    for i in range(N):
        C[i+1] = B[i+1]
    #Cの各要素の値を、出席番号に変換する
    #0番目は使わない
    D = [0] * (N+1)
    for i in range(N):
        D[C[i+1]] = i+1
    #出席番号の順に出力する
    for i in range(N):
        print(D[i+1], end=" ")
    print()
