def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    sum = 0
    for i in range(n):
        sum += b[i] * (b[i]-1) // 2
    for i in range(n):
        print(sum - b[a[i]-1] + 1)

if __name__ == '__main__':
    main()