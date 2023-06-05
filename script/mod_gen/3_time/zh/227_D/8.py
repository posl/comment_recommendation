def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    count = 0
    for i in range(k):
        count += a[i]
    print(count)

if __name__ == '__main__':
    main()