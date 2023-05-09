def main():
    #入力
    N = int(input())
    a = list(map(int, input().split()))
    #処理
    ans = len(set(a))
    #出力
    print(ans)
