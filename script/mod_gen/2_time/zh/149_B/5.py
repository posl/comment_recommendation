def main():
    a,b,k=map(int,input().split())
    for i in range(k):
        if i%2==0:
            if a%2==1:
                a-=1
            b+=a//2
            a=a//2
        else:
            if b%2==1:
                b-=1
            a+=b//2
            b=b//2
    print(a,b)

if __name__ == '__main__':
    main()