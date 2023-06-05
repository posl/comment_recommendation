def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = 0
    for i in range(n):
        b += 1 / a[i]
    print(1 / b)

if __name__ == '__main__':
    main()