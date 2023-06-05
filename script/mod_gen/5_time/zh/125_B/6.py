def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    max_value = 0
    for i in range(1 << n):
        value = 0
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                value += v[j]
                cost += c[j]
        max_value = max(max_value, value - cost)
    print(max_value)

if __name__ == '__main__':
    main()