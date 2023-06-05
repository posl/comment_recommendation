def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    sum_b = 0
    for i in range(m):
        if a[i] < sum_a / (4 * m):
            print("No")
            return
        sum_b += a[i]
    if sum_b >= sum_a / 4:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()