def main():
    A,B = map(int,input().split())
    if A > B:
        print(0)
    else:
        print(B-A)

if __name__ == '__main__':
    main()