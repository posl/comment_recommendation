def main():
    a,b,k=map(int,input().split())
    ans=""
    for i in range(a+b):
        if a==0:
            ans+="b"
            b-=1
            continue
        if b==0:
            ans+="a"
            a-=1
            continue
        if k<=combination(a+b-1,a-1):
            ans+="a"
            a-=1
        else:
            ans+="b"
            b-=1
            k-=combination(a+b,a-1)
    print(ans)

if __name__ == '__main__':
    main()