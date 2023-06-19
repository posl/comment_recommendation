def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        i = 0
        while i < N:
            if h[i] > 0:
                ans += 1
                while i < N and h[i] > 0:
                    h[i] -= 1
                    i += 1
            i += 1
    print(ans)

if __name__ == '__main__':
    main()