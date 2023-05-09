def main():
    #入力
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int,input().split())))
    #処理
    ans = "No"
    for i in range(n-2):
        if d[i][0]==d[i][1]==d[i+1][0]==d[i+1][1]==d[i+2][0]==d[i+2][1]:
            ans = "Yes"
            break
    #出力
    print(ans)
