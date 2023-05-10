def main():
    a,b,c,d = map(int,input().split())
    if d*c-b <= 0:
        print(-1)
        return
    if a <= b:
        print(0)
        return
    else:
        print((a-b-1)//(d*c-b)+1)

if __name__ == '__main__':
    main()