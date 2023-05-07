def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        #素数リストを作成
        prime_list = [2]
        for j in range(3, int(N**0.5)+1, 2):
            for k in prime_list:
                if j % k == 0:
                    break
            else:
                prime_list.append(j)
        #N=p^2qを満たす素数p,qを探す
        for p in prime_list:
            if N % p == 0:
                q = N // p
                if q % p == 0:
                    print(p, q // p)
                    break

if __name__ == '__main__':
    main()