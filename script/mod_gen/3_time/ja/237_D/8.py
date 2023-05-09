def main():
    n = int(input())
    s = input()
    # 0を含めた数列の長さ
    l = n + 1
    a = [0] * l
    # 0の位置
    zero = 0
    for i in range(n):
        if s[i] == "L":
            a[zero] = i + 1
            zero -= 1
        else:
            a[zero + 1] = i + 1
            zero += 1
    print(*a)

if __name__ == '__main__':
    main()