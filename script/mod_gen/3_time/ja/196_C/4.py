def main():
    N = int(input())
    # 1桁
    if N < 10:
        print(0)
        return
    # 2桁
    if N < 100:
        print(9)
        return
    # 3桁
    if N < 1000:
        print(9)
        return
    # 4桁
    if N < 10000:
        print(9*2)
        return
    # 5桁
    if N < 100000:
        print(9*3)
        return
    # 6桁
    if N < 1000000:
        print(9*4)
        return
    # 7桁
    if N < 10000000:
        print(9*5)
        return
    # 8桁
    if N < 100000000:
        print(9*6)
        return
    # 9桁
    if N < 1000000000:
        print(9*7)
        return
    # 10桁
    if N < 10000000000:
        print(9*8)
        return
    # 11桁
    if N < 100000000000:
        print(9*9)
        return
    # 12桁
    if N < 1000000000000:
        print(9*10)
        return
    # 13桁
    if N < 10000000000000:
        print(9*11)
        return
    # 14桁
    if N < 100000000000000:
        print(9*12)
        return

if __name__ == '__main__':
    main()