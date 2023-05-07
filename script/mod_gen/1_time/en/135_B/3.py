def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        if p[i] > p[i + 1]:
            cnt += 1
            if cnt > 1:
                print("NO")
                return
            if i + 2 < n and p[i + 2] < p[i]:
                p[i], p[i + 2] = p[i + 2], p[i]
            else:
                p[i], p[i + 1] = p[i + 1], p[i]
    print("YES")

if __name__ == '__main__':
    main()