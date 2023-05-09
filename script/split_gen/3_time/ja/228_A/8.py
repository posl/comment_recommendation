def main():
    #入力
    s, t, x = map(int, input().split())
    #出力
    print('Yes' if s <= x < t else 'No')
