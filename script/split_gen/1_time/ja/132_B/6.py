def main():
    #入力
    n = int(input())
    p = list(map(int, input().split()))
    #処理
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    #出力
    print(count)
