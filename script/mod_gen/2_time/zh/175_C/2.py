def main():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x/d >= k:
        print(x-d*k)
        return
    k -= x//d
    x %= d
    if k%2 == 0:
        print(x)
    else:
        print(abs(x-d))

if __name__ == '__main__':
    main()