def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    sum = 0
    for i in range(n):
        sum += a[i]
    k = x // sum
    x = x - sum * k
    for i in range(n):
        x = x - a[i]
        if x <= 0:
            print(i+1 + k*n)
            break

if __name__ == '__main__':
    main()