def main():
    N = int(input())
    #N = 10000000
    #N = 33
    #N = 1333
    #N = 1000000000000
    #N = 10000000000000
    #N = 100000000000000
    # 1桁の数は条件を満たさない
    if N < 10:
        print(0)
        return
    # 1桁の数は条件を満たさない
    if N < 100:
        print(1)
        return
    # 1桁の数は条件を満たさない
    if N < 1000:
        print(9)
        return
    # 1桁の数は条件を満たさない
    if N < 10000:
        print(9 + 9)
        return
    # 1桁の数は条件を満たさない
    if N < 100000:
        print(9 + 9 + 9)
        return
    # 1桁の数は条件を満たさない
    if N < 1000000:
        print(9 + 9 + 9 + 9)
        return
    # 1桁の数は条件を満たさない
    if N < 10000000:
        print(9 + 9 + 9 + 9 + 9)
        return
    # 1桁の数は条件を満たさない
    if N < 100000000:
        print(9 + 9 + 9 + 9 + 9 + 9)
        return
    # 1桁の数は条件を満たさない
    if N < 1000000000:
        print(9 + 9 + 9 + 9 + 9 + 9 + 9)
        return
    # 1桁の数は条件を満たさない
    if N < 10000000000:
        print(9 + 9 + 9 + 9 + 9 + 9 + 9 + 9)
        return
    # 1桁

if __name__ == '__main__':
    main()