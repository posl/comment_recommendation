def main():
    n = int(input())
    if -2**31 <= n <= 2**31 - 1:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()