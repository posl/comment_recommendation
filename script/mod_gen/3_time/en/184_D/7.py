def main():
    a,b,c=map(int,input().split())
    s=a+b+c
    print(1+((a/s)*(1+((a-1)/(s-1))))+((b/s)*(1+((b-1)/(s-1))))+((c/s)*(1+((c-1)/(s-1)))))

if __name__ == '__main__':
    main()