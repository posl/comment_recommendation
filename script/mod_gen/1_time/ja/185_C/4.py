def main():
    L = int(input())
    if L == 12:
        print(1)
    else:
        print((L - 12) * (L - 11) // 2)

if __name__ == '__main__':
    main()