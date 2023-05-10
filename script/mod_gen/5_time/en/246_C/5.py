def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    cost = 0
    for i in range(n):
        if k > 0:
            cost += min(a[i],x)
            k -= 1
        else:
            cost += a[i]
    print(cost)

if __name__ == '__main__':
    main()