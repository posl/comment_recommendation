def main():
    a,b,c,d = map(int,input().split())
    if a*60+b<c*60+d:
        print("高桥")
    else:
        print("青木")

if __name__ == '__main__':
    main()