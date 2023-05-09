def main():
    #入力
    N = int(input())
    #処理
    if -2**31 <= N < 2**31:
        print('Yes')
    else:
        print('No')
    #出力
