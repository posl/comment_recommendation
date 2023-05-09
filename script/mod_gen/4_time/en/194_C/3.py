def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(1,n):
        for j in range(0,i):
            sum += (a[i]-a[j])**2
    print(sum)

if __name__ == '__main__':
    main()