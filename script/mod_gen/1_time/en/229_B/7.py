def main():
    A,B = map(int,input().split())
    if A+B > 999999999:
        print("Hard")
    else:
        print("Easy")
main()

if __name__ == '__main__':
    main()