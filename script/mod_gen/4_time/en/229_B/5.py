def main():
    A, B = map(int, input().split())
    if A + B < 10:
        print("Easy")
    else:
        print("Hard")
    return

if __name__ == '__main__':
    main()