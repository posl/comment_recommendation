def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * 200000
    for i in range(n):
        c[a[i]] += 1
    for i in range(1, 200000):
        if c[i] > 0:
            for j in range(i, 200000, i):
                b[j-1] += c[i]
    for i in range(n):
        print(b[i])

if __name__ == '__main__':
    main()