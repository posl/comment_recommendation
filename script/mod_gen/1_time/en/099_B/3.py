def main():
    a,b = map(int,input().split())
    print((b*(b+1)//2)-(a*(a-1)//2)-b+a-1)

if __name__ == '__main__':
    main()