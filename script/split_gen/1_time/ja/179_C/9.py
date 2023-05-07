def main():
    N = int(input()) #問題文の制約より、Nは2以上10^6以下の正整数
    ans = 0
    for i in range(1, N+1):
        ans += (N-1)//i
    print(ans)
