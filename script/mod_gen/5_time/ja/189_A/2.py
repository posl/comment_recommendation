def solve():
    # coding: utf-8
    # Your code here!
    #文字列の入力
    s = input()
    #出力
    if s[0] == s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

if __name__ == '__main__':
    solve()