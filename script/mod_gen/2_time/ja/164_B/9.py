def main():
    A, B, C, D = map(int, input().split())
    #高橋君のモンスターの攻撃回数
    a = (C + B - 1) // B
    #青木君のモンスターの攻撃回数
    b = (A + D - 1) // D
    if a <= b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()