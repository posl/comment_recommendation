def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            l = 0
            r = 0
            for i in range(N):
                if h[i] > 0:
                    l = i
                    break
            for i in range(l,N):
                if h[i] == 0:
                    r = i
                    break
                elif i == N-1:
                    r = N
            for i in range(l,r):
                h[i] -= 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()