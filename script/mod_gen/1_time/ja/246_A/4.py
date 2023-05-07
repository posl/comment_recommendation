def main():
    #入力
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    #出力
    if (x1 == x2):
        print(x3, end = " ")
    elif (x1 == x3):
        print(x2, end = " ")
    else:
        print(x1, end = " ")
    if (y1 == y2):
        print(y3, end = " ")
    elif (y1 == y3):
        print(y2, end = " ")
    else:
        print(y1, end = " ")
main()

if __name__ == '__main__':
    main()