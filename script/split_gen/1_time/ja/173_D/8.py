def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    
    #Aを降順にソート
    A.sort(reverse=True)
    
    #Aの降順ソートの最初の要素と最後の要素をそれぞれ最初と最後に配置する
    #その時の心地よさの合計を求める
    ans = A[0] + A[-1]
    
    #Aの降順ソートの2番目からN-1番目の要素をそれぞれ順番に配置する
    #その時の心地よさの合計を求める
    for i in range(1, N-1):
        ans += min(A[i], A[i+1])
    
    #出力
    print(ans)
