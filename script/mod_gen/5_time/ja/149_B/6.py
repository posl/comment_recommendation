def main():
    a,b,k=map(int,input().split())
    if k>=a:
        k=k-a
        a=0
    else:
        a=a-k
        k=0
    if k>=b:
        k=k-b
        b=0
    else:
        b=b-k
        k=0
    print(a,b)
main()

if __name__ == '__main__':
    main()