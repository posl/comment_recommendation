def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n - 1):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

if __name__ == '__main__':
    main()