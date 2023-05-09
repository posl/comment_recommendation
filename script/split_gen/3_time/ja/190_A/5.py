def main():
    # 標準入力から A, B, C を取得する
    A, B, C = map(int, input().split())
    # ここにプログラムを追記
    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if B > A:
            print('Aoki')
        else:
            print('Takahashi')
