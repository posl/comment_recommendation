def main():
    n = int(input())
    d = [0]*(10**9+2)
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] += 1
        d[a+b] -= 1
    for i in range(1, 10**9+2):
        d[i] += d[i-1]
    print(*d[1:-1])

if __name__ == '__main__':
    main()