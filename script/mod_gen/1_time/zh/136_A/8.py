def main():
    a,b,c = map(int,input().split())
    if a < b+c:
        print(b+c-a)
    else:
        print(0)

if __name__ == '__main__':
    main()