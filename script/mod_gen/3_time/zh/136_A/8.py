def main():
    a,b,c = map(int,input().split())
    if b >= a:
        print(c)
    else:
        print(c-(a-b))

if __name__ == '__main__':
    main()