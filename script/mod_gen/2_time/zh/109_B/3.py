def main():
    A,B = map(int,input().split())
    if A*B*3%2 != 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()