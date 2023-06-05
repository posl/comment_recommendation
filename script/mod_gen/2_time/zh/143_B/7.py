def main():
    a,b = map(int,input().split())
    if a > b:
        print(a-b)
    else:
        print(0)

if __name__ == '__main__':
    main()