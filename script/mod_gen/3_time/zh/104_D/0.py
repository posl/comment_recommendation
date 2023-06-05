def main():
    S = input()
    Q = S.count("?")
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    ans = 0
    for i in range(Q+1):
        for j in range(Q+1-i):
            k = Q-i-j
            ans += (pow(3,i,1000000007)*pow(3,j,1000000007)*pow(3,k,1000000007)*comb(A+i-1,i)*comb(B+j-1,j))%1000000007
    print(ans%1000000007)

if __name__ == '__main__':
    main()