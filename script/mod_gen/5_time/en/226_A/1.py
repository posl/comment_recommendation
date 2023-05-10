def main():
    x = float(input())
    if x < 0:
        print(0)
    elif x < 100:
        print(int(x))
    else:
        print(100)

if __name__ == '__main__':
    main()