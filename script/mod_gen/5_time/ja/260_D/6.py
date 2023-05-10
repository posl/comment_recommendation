def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print()
    #カードの食べられるターンを記録するリスト
    eat_turn = [0] * N
    #カードの場に置かれるターンを記録するリスト
    put_turn = [0] * N
    #カードの場に置かれているかどうかを記録するリスト
    is_put = [0] * N
    #カードを置く
    for i in range(N):
        #print("i", i)
        #print("P[i]", P[i])
        #print("put_turn", put_turn)
        #print("is_put", is_put)
        #print()
        #場にカードを置く
        is_put[P[i]-1] = 1
        #カードの場に置かれたターンを記録する
        put_turn[P[i]-1] = i+1
        #場に置かれているカードの枚数を数える
        count = 0
        for j in range(N):
            if is_put[j] == 1:
                count += 1
        #print("count", count)
        #場に置かれたカードがK枚に達した場合、カードを食べる
        if count >= K:
            #print("eat")
            #カードを食べる
            for j in range(N):
                if is_put[j] == 1:
                    #カードの食べられたターンを記録する
                    eat_turn[j] = i+1
                    #カードを場から消す
                    is_put[j] = 0
            #print("eat_turn", eat_turn)
            #print("is_put", is_put)
            #print()
    #カードを食べられなかったカードの食べられなかったことを記録する
    for i in range(N):
        if

if __name__ == '__main__':
    main()