def main():
    n,k = map(int,input().split())
    i = 0
    while n >= k:
        n //= k
        i += 1
    print(i+1)

if __name__ == '__main__':
    main()