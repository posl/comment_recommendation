def main():
    a, b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        print("输入的所有数值都是整数，而且1 ≦ A ≦ 20, 1 ≦ B ≦ 20")
        return
    print(a * b)

if __name__ == '__main__':
    main()