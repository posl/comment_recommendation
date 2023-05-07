def main():
    N = int(input())
    if N < 4:
        print("No")
        return
    if N % 4 == 0 or N % 7 == 0 or N % 4 == 2:
        print("Yes")
        return
    print("No")
main()

if __name__ == '__main__':
    main()