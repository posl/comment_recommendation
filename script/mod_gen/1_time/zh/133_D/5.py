def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - b[i - 1] // 2 - b[(i + 1) % n] // 2
    print(*b)

if __name__ == '__main__':
    resolve()