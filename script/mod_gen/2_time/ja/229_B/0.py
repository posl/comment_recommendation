def main():
    A, B = map(int, input().split())
    if A + B >= 10**18:
        print("Hard")
    else:
        print("Easy")

if __name__ == '__main__':
    main()