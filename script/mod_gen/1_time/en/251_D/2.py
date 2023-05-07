def main():
    w = int(input())
    if w <= 2:
        print(1)
        print(w)
    elif w <= 4:
        print(2)
        print(1, w-1)
    elif w <= 300:
        print(3)
        print(1, 2, 3)
    else:
        print(6)
        print(2, 5, 1, 2, 5, 1)

if __name__ == '__main__':
    main()