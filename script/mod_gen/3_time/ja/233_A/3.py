def main():
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
        return
    print((Y - X + 9) // 10)

if __name__ == '__main__':
    main()