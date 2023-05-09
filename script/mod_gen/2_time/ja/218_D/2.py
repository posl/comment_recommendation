def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if x[i] == x[j] and y[j] == y[k] and x[k] == x[i]:
                    ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()