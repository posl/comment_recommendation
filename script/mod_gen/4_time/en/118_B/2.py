def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k, *a = map(int, input().split())
        for j in range(k):
            foods[a[j] - 1] += 1
    print(sum(1 for i in foods if i == n))

if __name__ == '__main__':
    main()