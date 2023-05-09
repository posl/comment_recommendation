def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    happiness = 0
    for i in range(n):
        happiness += b[a[i]-1]
        if i < n-1 and a[i]+1 == a[i+1]:
            happiness += c[a[i]-1]
    print(happiness)

if __name__ == '__main__':
    main()