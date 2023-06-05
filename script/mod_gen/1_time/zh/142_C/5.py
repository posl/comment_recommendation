def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    for i in range(n):
        print(b[i], end=" ")

if __name__ == '__main__':
    main()