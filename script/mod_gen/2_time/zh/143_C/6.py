def main():
    n = int(input())
    d = list(map(int, input().split()))
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += d[i] * d[j]
    print(total)

if __name__ == '__main__':
    main()