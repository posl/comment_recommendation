def main():
    A, B = map(int, input().split())
    if A+B<10:
        print("Easy")
    else:
        print("Hard")
main()

if __name__ == '__main__':
    main()