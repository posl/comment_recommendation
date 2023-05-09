def main():
    a,b,c,d = map(int,input().split())
    if (c*60+d)-(a*60+b) > 0:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()