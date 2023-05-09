def main():
    L = int(input())
    if L % 3 == 0:
        print((L // 3) ** 3)
    else:
        print((L // 3) ** 3 * (L % 3))

if __name__ == '__main__':
    main()