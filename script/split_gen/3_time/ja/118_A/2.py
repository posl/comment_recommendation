def main():
    #入力
    a, b = map(int, input().split())
    #出力
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)
