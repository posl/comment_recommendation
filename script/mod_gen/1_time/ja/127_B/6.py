def main():
    #入力
    r, D, x2000 = map(int, input().split())
    #出力
    for i in range(10):
        x = r * x2000 - D
        print(x)
        x2000 = x

if __name__ == '__main__':
    main()