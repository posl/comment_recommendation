def main():
    N = int(input())
    if N % 10 == 7 or (N // 10) % 10 == 7 or (N // 100) % 10 == 7:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()