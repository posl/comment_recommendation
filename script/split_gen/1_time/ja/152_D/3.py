def main():
    # 入力
    N = int(input())
    # 処理
    ans = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if i%10==j//10%10 and i//10%10==j%10:
                ans += 1
    # 出力
    print(ans)
