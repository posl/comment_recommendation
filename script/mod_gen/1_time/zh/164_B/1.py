def main():
    a,b,c,d = map(int,input().split())
    if (c-1)//b > (a-1)//d:
        print("否")
    else:
        print("是")

if __name__ == '__main__':
    main()