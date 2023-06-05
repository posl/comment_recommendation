def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    max_a = max(a)
    min_b = min(b)
    max_b = max(b)
    if max_a - min_a > k or max_b - min_b > k:
        print("No")
        exit()
    for i in range(n):
        if a[i] + b[i] < k:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()