def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x//d >= k:
        print(x-d*k)
    else:
        if (k-x//d)%2 == 0:
            print(x%d)
        else:
            print(abs(x%d-d))

if __name__ == '__main__':
    main()