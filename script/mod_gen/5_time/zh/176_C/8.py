def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        if a[i] < a[i+1]:
            b[i+1] = b[i] + 1
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1] and b[i-1] <= b[i]:
            b[i-1] = b[i] + 1
    print(sum(b) + n)

if __name__ == '__main__':
    main()