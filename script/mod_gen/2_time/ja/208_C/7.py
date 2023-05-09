def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 国民番号でソート
    A.sort()
    
    # お菓子の配り方の総数
    cnt = K // N
    
    # 1人あたりのお菓子の個数
    for i in range(N):
        if A[i] <= cnt:
            print(cnt)
        else:
            print(K // N + 1)
    
    # 余ったお菓子の配り方
    mod = K % N
    
    # 余ったお菓子の配り方の総数
    cnt = cnt + 1
    
    # 余ったお菓子の配り方で配る人数
    for i in range(mod):
        print(cnt)
main()

if __name__ == '__main__':
    main()