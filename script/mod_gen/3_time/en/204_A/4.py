def main():
    x, y = input().split()
    if x == y:
        print(x)
    else:
        print(str(3 - int(x) - int(y)))

if __name__ == '__main__':
    main()