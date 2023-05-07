def main():
    L = int(input())
    if L % 3 == 0:
        print((L / 3) ** 3)
        return
    if L % 2 == 0:
        print((L / 2) ** 3 / 8)
        return
    else:
        print((L - 1) * (L - 2) * (L - 3) / 6)

if __name__ == '__main__':
    main()