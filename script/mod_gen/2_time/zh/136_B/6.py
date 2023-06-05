def main():
    a,b,c = map(int,input().split())
    if b+c<a:
        print(c)
    else:
        print(a-b)

if __name__ == '__main__':
    main()