def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    b.append(0)
    for i in range(n):
        b.append(a[i])
    b.append(0)
    sum = 0
    for i in range(n+1):
        sum += abs(b[i+1]-b[i])
    sum += abs(b[n+1])
    for i in range(n):
        print(sum-abs(b[i+1]-b[i])-abs(b[i+2]-b[i+1])+abs(b[i+2]-b[i]))
    print(sum-abs(b[n+1]-b[n])-abs(b[n]-b[n-1])+abs(b[n+1]-b[n-1]))

if __name__ == '__main__':
    main()