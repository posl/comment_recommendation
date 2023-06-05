def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    t %= sum
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]
main()
