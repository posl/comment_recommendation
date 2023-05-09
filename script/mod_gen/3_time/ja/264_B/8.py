def main():
    # R:行数、C:列数
    R, C = map(int, input().split())
    # グリッドの塗り分け
    if (R * C) % 2 == 0:
        print("white")
    else:
        print("black")

if __name__ == '__main__':
    main()