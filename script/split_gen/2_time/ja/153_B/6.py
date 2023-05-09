def main():
    # 入力
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    if H <= sum(A):
        ans = "Yes"
    else:
        ans = "No"
    # 出力
    print(ans)
