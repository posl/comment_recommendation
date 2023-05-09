def main():
    N, A, B = map(int, input().split())
    #Aの倍数の数
    A_count = N//A
    #Bの倍数の数
    B_count = N//B
    #AとBの最小公倍数
    C = A*B//math.gcd(A,B)
    #Cの倍数の数
    C_count = N//C
    #AとBの最小公倍数を含む総和
    print(A_count*B_count*C_count - C_count*(C_count+1)//2*C)

if __name__ == '__main__':
    main()