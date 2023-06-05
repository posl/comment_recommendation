def main():
    n,k = map(int,input().split())
    while True:
        if n<k:
            break
        else:
            n = n%k
            if n>k:
                n = k-n
    print(n)
main()
