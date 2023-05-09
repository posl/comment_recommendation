def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0] * (n + 1)
    for i in c:
        d[i] += 1
    count = 0
    for i in range(n):
        count += d[a[i]] * b[i]
    print(count)

if __name__ == '__main__':
    main()