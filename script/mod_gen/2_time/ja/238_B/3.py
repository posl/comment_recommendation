def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        a_sum = 0
        for j in range(n):
            if i == j:
                continue
            a_sum += a[j]
            if a_sum >= 360:
                a_sum -= 360
        if a_sum > max:
            max = a_sum
    print(max)

if __name__ == '__main__':
    main()