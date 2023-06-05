def main():
    a,b,c,d = map(int,input().split())
    if a < c or (a == c and b < d):
        print("高桥")
    else:
        print("青木")

if __name__ == '__main__':
    main()