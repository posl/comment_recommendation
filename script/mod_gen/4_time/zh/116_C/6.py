def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while h[i] > 0:
            for j in range(i, n):
                if h[j] == 0:
                    break
                h[j] -= 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()