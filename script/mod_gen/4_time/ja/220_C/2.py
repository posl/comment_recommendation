def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    k = x // sum_a
    x -= sum_a * k
    sum_a = sum(a[:k])
    for i in range(n):
        if sum_a > x:
            break
        sum_a += a[i]
        k += 1
    print(k)

if __name__ == '__main__':
    main()