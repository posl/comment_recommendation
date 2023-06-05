def main():
    n = int(input())
    digit = 0
    for i in range(1, 16):
        if n < 10 ** i:
            digit = i
            break
    if digit <= 3:
        print(0)
        return
    elif digit <= 6:
        print(n - 999)
        return
    elif digit <= 9:
        print((n - 999999) * 2 + 999000)
        return
    elif digit <= 12:
        print((n - 999999999) * 3 + 1998000)
        return
    elif digit <= 15:
        print((n - 999999999999) * 4 + 2999700000)
        return
    else:
        print(107730272137364)

if __name__ == '__main__':
    main()