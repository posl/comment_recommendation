def main():
    # Y: 2000 ≦ Y ≦ 3000
    Y = int(input())
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + 4 - Y % 4)

if __name__ == '__main__':
    main()