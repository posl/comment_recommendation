def main():
    n = int(input())
    p = list(map(lambda x: int(x)-1, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()