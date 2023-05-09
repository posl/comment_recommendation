def main():
    n, k = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort()
    ans = k
    for i in range(n):
        a, b = ab[i]
        if ans < a:
            break
        ans += b
    print(ans)

if __name__ == '__main__':
    main()