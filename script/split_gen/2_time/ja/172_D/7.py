def main():
    N = int(input())
    ans = 0
    # 約数の個数を求める
    for i in range(1,N+1):
        ans += i * (N//i)
    print(ans)
