def main():
    #入力
    N = int(input())
    H = list(map(int,input().split()))
    #処理
    max = 0
    for i in range(0,N):
        if H[i] > max:
            max = H[i]
            ans = i + 1
    #出力
    print(ans)
