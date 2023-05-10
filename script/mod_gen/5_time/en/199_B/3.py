def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    for i in range(n):
        x = max(x, a[i])
    for i in range(n):
        x = min(x, b[i])
    print(x)

if __name__ == '__main__':
    main()