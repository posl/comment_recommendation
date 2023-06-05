def main():
    n = int(input())
    d = [0] * (10**9 + 1)
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] += 1
        d[a+b] -= 1
    for i in range(10**9):
        d[i+1] += d[i]
    print(*d[1:])

if __name__ == '__main__':
    main()