def main():
    #入力
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    
    #処理
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
            
    #出力
    print(count)
