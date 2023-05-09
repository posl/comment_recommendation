def main():
    N = int(input())
    print("Yes" if N % 4 == 0 or N % 7 == 0 or N % 4 == 7 or N % 7 == 4 else "No")

if __name__ == '__main__':
    main()