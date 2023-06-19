def main():
    #输入
    P = int(input())
    #计算
    #先得到能够凑出P的最大的N！
    N = 1
    while True:
        if P < N*(N+1):
            N -= 1
            break
        else:
            N += 1
    #print(N)
    #得到N！
    N_fac = 1
    for i in range(1,N+1):
        N_fac *= i
    #print(N_fac)
    #得到N!的倍数
    N_fac_mul = 1
    for i in range(1,N+1):
        N_fac_mul *= N_fac
    #print(N_fac_mul)
    #得到P的倍数
    P_mul = 1
    for i in range(1,P//N_fac+1):
        P_mul *= P
    #print(P_mul)
    #得到余数
    Remainder = P_mul % N_fac_mul
    #print(Remainder)
    #得到需要的硬币数
    if Remainder == 0:
        Coin = P//N_fac
    else:
        Coin = P//N_fac + 1
    #输出
    print(Coin)
