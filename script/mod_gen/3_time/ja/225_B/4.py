def main():
    N = int(input())
    deg = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        deg[a] += 1
        deg[b] += 1
    if deg.count(1) == 1 and deg.count(N - 1) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()