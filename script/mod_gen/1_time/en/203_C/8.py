def main():
    n, k = map(int, input().split())
    village = []
    for i in range(n):
        a, b = map(int, input().split())
        village.append((a, b))
    village.sort()
    ans = 0
    for i in range(n):
        if k >= village[i][0] - ans:
            k += village[i][1]
        else:
            ans += k
            break
    else:
        ans += k
    print(ans)

if __name__ == '__main__':
    main()