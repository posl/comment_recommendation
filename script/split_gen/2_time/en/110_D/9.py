def main():
    N, M = map(int, input().split())
    #Mの素因数分解
    M_factor = []
    i = 2
    while i * i <= M:
        if M % i == 0:
            M_factor.append(i)
            M //= i
        else:
            i += 1
    if M > 1:
        M_factor.append(M)
    #Mの素因数の個数を求める
    M_factor_num = []
    for i in M_factor:
        M_factor_num.append(M_factor.count(i))
    #Mの素因数の個数をN乗する
    M_factor_num = [i * N for i in M_factor_num]
    #N乗した個数を素因数分解する
    M_factor_num2 = []
    for i in M_factor_num:
        i_factor = []
        j = 2
        while j * j <= i:
            if i % j == 0:
                i_factor.append(j)
                i //= j
            else:
                j += 1
        if i > 1:
            i_factor.append(i)
        M_factor_num2.append(i_factor)
    #Mの素因数の個数をN乗した素因数の個数をMの素因数の個数で割る
    M_factor_num3 = []
    for i in range(len(M_factor_num2)):
        M_factor_num3.append([])
        for j in M_factor_num2[i]:
            M_factor_num3[i].append(M_factor_num2[i].count(j) // M_factor_num[i])
    #Mの素因数の個数をN乗した素因数の個数をMの素因数の個数で割った個数を求める
    M_factor_num4 = []
    for i in M_factor_num3:
        M_factor_num4.append(1)
        for j in i:
            M_factor_num4[-1] *= (j + 1)
    #Mの素因数の個数をN乗した素因数の個数をMの素因数の個数で割った個数の積を求める
    M_factor_num
