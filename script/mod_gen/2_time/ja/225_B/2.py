def main():
    n = int(input())
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        deg[a] += 1
        deg[b] += 1
    if deg.count(n - 1) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()