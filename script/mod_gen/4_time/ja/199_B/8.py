def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    for i in range(1, 1000 + 1):
        if all(a[j] <= i <= b[j] for j in range(n)):
            x += 1
    print(x)

if __name__ == '__main__':
    main()