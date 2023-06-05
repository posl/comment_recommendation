def main():
    n = int(input())
    if n % 10 == 7:
        print("是")
    elif n // 10 % 10 == 7:
        print("是")
    elif n // 100 % 10 == 7:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()