def main():
    # 入力
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # 処理
    ans = max(abs(a - d), abs(b - c), abs(a - c), abs(b - d))
    
    # 出力
    print(ans)
