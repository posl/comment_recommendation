def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cost = 0
    for i in range(n):
        if k > 0:
            if a[i] < x:
                cost += a[i]
                k -= 1
            else:
                cost += x
        else:
            cost += a[i]
    print(cost)

if __name__ == '__main__':
    main()