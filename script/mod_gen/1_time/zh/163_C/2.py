def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[a[i]] += 1
    for i in range(1, n + 1):
        print(b[i])

if __name__ == '__main__':
    main()