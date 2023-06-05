def main():
    X = float(input())
    x = int(X)
    y = X - x
    if y < 0.25:
        print(x)
    elif y < 0.75:
        print(x+0.5)
    else:
        print(x+1)

if __name__ == '__main__':
    main()