def main():
    A, B = map(int, input().split())
    if B > A * 6:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()