def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if i == n-1:
            if a[0] - a[i] > max:
                max = a[0] - a[i]
        else:
            if a[i+1] - a[i] > max:
                max = a[i+1] - a[i]
    print(k-max)
main()
