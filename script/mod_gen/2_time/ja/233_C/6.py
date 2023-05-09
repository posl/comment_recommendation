def main():
    #データ入力
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #Xの素因数分解
    X_list = prime_factorize(X)
    #Aの素因数分解
    A_list = []
    for i in range(N):
        A_list.append([])
        for j in range(1, A[i][0]+1):
            A_list[i].append(prime_factorize(A[i][j]))
    #Aの素因数分解のリストを1つのリストにまとめる
    A_list_sum = []
    for i in range(N):
        A_list_sum += A_list[i]
    #Xの素因数分解をAの素因数分解のリストにあるかどうかでカウントする
    count = 0
    for i in range(len(X_list)):
        if X_list[i] in A_list_sum:
            count += 1
    #Xの素因数分解の数と一致したらOK
    if count == len(X_list):
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()