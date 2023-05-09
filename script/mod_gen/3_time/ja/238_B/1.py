def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        total = 0
        for j in range(n):
            total += a[(i+j) % n]
            if total > max:
                max = total
    print(max)

if __name__ == '__main__':
    main()