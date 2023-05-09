def main():
    #入力
    R, X, Y = map(int, input().split())
    #出力
    print(1 + ((X**2 + Y**2)**(1/2) // R) + (1 if (X**2 + Y**2)**(1/2) % R != 0 else 0))

if __name__ == '__main__':
    main()