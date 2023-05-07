def main():
    N = int(input())
    h = list(map(int,input().split()))
    ans = 0
    while sum(h) > 0:
        i = 0
        while i < N:
            if h[i] > 0:
                j = i
                while j < N and h[j] > 0:
                    h[j] -= 1
                    j += 1
                ans += 1
            i += 1
    print(ans)

if __name__ == '__main__':
    main()