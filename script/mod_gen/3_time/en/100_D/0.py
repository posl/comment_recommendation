def main():
    N, M = map(int, input().split())
    x = [0] * N
    y = [0] * N
    z = [0] * N
    for i in range(N):
        x[i], y[i], z[i] = map(int, input().split())
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a = []
                for l in range(N):
                    if i == 0:
                        a.append(x[l] + y[l] + z[l])
                    else:
                        a.append(-x[l] - y[l] - z[l])
                a.sort(reverse=True)
                if j == 0:
                    ans = max(ans, sum(a[:M]))
                else:
                    ans = max(ans, -sum(a[:M]))
    print(ans)

if __name__ == '__main__':
    main()