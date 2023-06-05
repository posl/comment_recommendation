def main():
    a,b,c,d = map(int,input().split())
    if (a<b):
        print(-1)
    else:
        if (c*d-b<=0):
            print(-1)
        else:
            print((a+b-1)//(c*d-b))

if __name__ == '__main__':
    main()