def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        sum += (a[i] - a[0]) + (a[n-1] - a[i])
    print(sum)
main()
