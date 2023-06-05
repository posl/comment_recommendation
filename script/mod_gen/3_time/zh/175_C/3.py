def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x//d >= k:
        print(x-d*k)
    else:
        k -= x//d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d-x)

if __name__ == '__main__':
    main()