def main():
    w = int(input())
    if w <= 3:
        print(1)
        print(w)
        return
    if w <= 5:
        print(2)
        print(2, w-2)
        return
    print(3)
    print(2, 3, w-5)
    return

if __name__ == '__main__':
    main()