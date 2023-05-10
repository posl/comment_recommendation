def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #Kの最大桁数を求める
    K_len = len(str(bin(K))[2:])
    #Kの最大桁数分のフラグを立てる
    K_flag = [0 for i in range(K_len)]
    #Aの最大桁数を求める
    A_max_len = 0
    for i in range(N):
        A_len = len(str(bin(A[i]))[2:])
        if A_len > A_max_len:
            A_max_len = A_len
    #Aの最大桁数分のフラグを立てる
    A_flag = [0 for i in range(A_max_len)]
    #Kの最大桁数分のフラグを立てる
    for i in range(K_len):
        K_flag[i] = 1
    #Aの最大桁数分のフラグを立てる
    for i in range(A_max_len):
        A_flag[i] = 1
    #Kの最大桁数分のフラグを立てる
    for i in range(K_len):
        K_flag[i] = 0
    #Aの最大桁数分のフラグを立てる
    for i in range(A_max_len):
        A_flag[i] = 0
    #Kの最大桁数分のフラグを立てる
    for i in range(K_len):
        K_flag[i] = 1
        K = 0
        for j in range(K_len):
            if K_flag[j] == 1:
                K += 2 ** j
        if K > K:
            K_flag[i] = 0
    #Aの最大桁数分のフラグを立てる
    for i in range(A_max_len):
        A_flag[i] = 1
        A = 0
        for j in range(A_max_len):
            if A_flag[j] == 1:
                A += 2 ** j
        if A > A:
            A_flag[i] = 0
    #Kの最大桁数分の

if __name__ == '__main__':
    main()