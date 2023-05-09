def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    #print(a)
    sum = 0
    for i in range(1, n + 1):
        sum += i * (a[i] ** 2)
    #print(sum)
    for i in range(1, n + 1):
        sum -= 2 * a[i] * (sum_a(a, i, n))
    print(sum)

if __name__ == '__main__':
    main()