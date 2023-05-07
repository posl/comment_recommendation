def main():
    A,B = map(int,input().split())
    if A%2==0:
        if B%2==0:
            print((B-A)//2)
        else:
            print((B-A)//2^B)
    else:
        if B%2==0:
            print((B-A)//2^A)
        else:
            print((B-A)//2)

if __name__ == '__main__':
    main()