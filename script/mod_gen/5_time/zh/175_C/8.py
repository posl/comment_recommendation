def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x > k*d:
        print(x-k*d)
    else:
        t = x//d
        if (k-t)%2==0:
            print(x%d)
        else:
            print(d-x%d)

if __name__ == '__main__':
    main()