def main():
    a,b,c = map(int,input().split())
    if c <= a - b:
        print(c)
    else:
        print(a-b)

if __name__ == '__main__':
    main()