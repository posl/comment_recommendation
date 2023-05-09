def main():
    x, y = map(int, input().split())
    if x >= 0 and x <= 100 and y >= 0 and y <= 100:
        if x * 4 >= y and x * 2 <= y:
            print("Yes")
        else:
            print("No")
    else:
        print("入力値が範囲外です")

if __name__ == '__main__':
    main()