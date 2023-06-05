def main():
    A,B = map(int, input().split())
    sum = A + B
    if sum < 10:
        print("Easy")
    else:
        print("Hard")

if __name__ == '__main__':
    main()