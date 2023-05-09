def main():
    #入力
    n = int(input())
    #16進数に変換
    n = hex(n)
    #先頭の0xを削除
    n = n[2:]
    #出力
    print(n.upper().zfill(2))
