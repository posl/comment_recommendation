def main():
    x = float(input())
    if x < 0.0:
        print(0)
    else:
        if x < 0.5:
            print(0)
        elif x < 1.0:
            print(1)
        else:
            print(int(x // 1 + 1))

if __name__ == '__main__':
    main()