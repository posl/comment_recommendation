def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    if sum_a == x:
        print(n)
        return
    k = x // sum_a
    x -= sum_a * k
    for i in range(n):
        x -= a[i]
        if x < 0:
            print(n * k + i + 1)
            return

if __name__ == '__main__':
    main()