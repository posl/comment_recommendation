def main():
    a,b,c = map(int, input().split())
    if(b//a < c):
        print(b//a)
    else:
        print(c)

if __name__ == '__main__':
    main()