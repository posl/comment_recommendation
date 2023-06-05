def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    x = int(input())
    sum_a = sum(a)
    k = x // sum_a
    x = x - k * sum_a
    if x == 0:
        print(k * n)
        return
    i = 0
    while x > 0:
        x -= a[i]
        i += 1
    print(k * n + i)

if __name__ == '__main__':
    main()