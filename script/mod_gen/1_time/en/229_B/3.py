def main():
    A,B = map(int, input().split())
    if len(str(A+B)) == len(str(A)) or len(str(A+B)) == len(str(B)):
        print("Easy")
    else:
        print("Hard")

if __name__ == '__main__':
    main()