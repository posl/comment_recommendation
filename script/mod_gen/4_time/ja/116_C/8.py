def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            for i in range(N):
                if h[i] > 0:
                    ans += 1
                    h[i] -= 1
                else:
                    continue
    print(ans)

if __name__ == '__main__':
    main()