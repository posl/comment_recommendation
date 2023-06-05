def main():
    N = int(input())
    if N % 10 == 7 or N // 10 % 10 == 7 or N // 100 % 10 == 7:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()