def main():
    A, B = map(int, input().split())
    sum = A + B
    if sum >= 10**18:
        print("Hard")
    else:
        print("Easy")

if __name__ == '__main__':
    main()