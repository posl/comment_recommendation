def main():
    N = int(input())
    L = []
    for _ in range(N):
        a, b = map(int, input().split())
        L.append((a, b))
    L.sort(key=lambda x: x[0])
    ans = 0
    for a, b in L:
        ans = max(ans, b)
    print(ans)

if __name__ == '__main__':
    main()