def main():
    n,k = map(int,input().split())
    count = 0
    while n >= k:
        n = n // k
        count += 1
    print(count+1)

if __name__ == '__main__':
    main()