def main():
    a,b,c,d = map(int,input().split())
    if a <= b*d:
        print(-1)
        return
    else:
        if a % (b*d-c) == 0:
            print(a//(b*d-c))
        else:
            print(a//(b*d-c)+1)

if __name__ == '__main__':
    main()