def main():
    n,k = map(int,input().split())
    p = [int(i) for i in input().split()]
    for i in range(k,n+1):
        print(sorted(p[:i])[-k])

if __name__ == '__main__':
    main()