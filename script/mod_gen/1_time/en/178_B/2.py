def main():
    a,b,c,d = map(int,input().split())
    if b*c >= a*d:
        print(b*c)
    else:
        print(a*d)

if __name__ == '__main__':
    main()