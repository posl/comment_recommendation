def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    cnt = 0
    ans = 0
    for i in range(n):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    print(ans)

if __name__ == '__main__':
    main()