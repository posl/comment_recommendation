def main():
    N, M, K = map(int, input().split())
    #友達関係のリスト
    friends = [[] for _ in range(N)]
    #ブロック関係のリスト
    blocks = [[] for _ in range(N)]
    #友達関係のリストを作る
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    
    #ブロック関係のリストを作る
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    #友達候補の数を数える
    for i in range(N):
        #友達候補の数
        ans = 0
        #友達候補の数を数える
        for j in friends[i]:
            #友達関係にある人の友達候補を数える
            ans += len(friends[j])
            #ブロック関係にある人の友達候補を引く
            for k in blocks[j]:
                if k in friends[i]:
                    ans -= 1
        #友達関係にある人の友達候補を引く
        for j in friends[i]:
            ans -= len(friends[j])
        #ブロック関係にある人の友達候補を引く
        for j in blocks[i]:
            ans -= len(friends[j])
        #友達候補の数を出力
        print(ans, end=' ')
    print()

if __name__ == '__main__':
    main()