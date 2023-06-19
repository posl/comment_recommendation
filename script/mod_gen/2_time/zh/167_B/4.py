def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
        return
    k = k - a
    if b >= k:
        print(a)
        return
    k = k - b
    print(a-k)

if __name__ == '__main__':
    main()