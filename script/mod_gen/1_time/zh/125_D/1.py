def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += abs(a[i])
    if a[0] < 0:
        a[0] = -a[0]
    for i in range(1, n):
        if a[i] < 0:
            a[i] = -a[i]
        if a[i-1] < a[i]:
            a[i-1], a[i] = a[i], a[i-1]
    if n % 2 == 0:
        print(sum)
    else:
        print(sum - 2*a[n-1])
main()
