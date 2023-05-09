def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    
    #初期状態の不便さ
    ans = (N-1)*(N-2)//2
    #print(ans)
    
    #各島が何個の島とつながっているか
    #島番号をインデックスとして使うため、0番目をダミーとして1から使う
    connect = [0] * (N+1)
    #print(connect)
    
    #各島が何個の島とつながっているかを調べる
    for i in range(M):
        connect[A[i]] += 1
        connect[B[i]] += 1
    #print(connect)
    
    #各島が何個の島とつながっているかをもとに不便さを計算する
    for i in range(M):
        #print(i)
        #print(ans)
        #print(connect[A[i]])
        #print(connect[B[i]])
        ans -= connect[A[i]]-1
        ans -= connect[B[i]]-1
        connect[A[i]] = 0
        connect[B[i]] = 0
        print(ans)

if __name__ == '__main__':
    main()