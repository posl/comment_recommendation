def main():
    #入力
    P = list(map(int, input().split()))
    #出力
    print(''.join([chr(i+96) for i in P]))
main()
