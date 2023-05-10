def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = a[0]
    stools = [0] * n
    for i in range(1, n):
        stools[i] = max_a - a[i]
        if a[i] > max_a:
            max_a = a[i]
    print(sum(stools))

if __name__ == '__main__':
    main()