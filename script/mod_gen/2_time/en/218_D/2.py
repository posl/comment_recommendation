def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if x[i] == x[j]:
                for k in range(j+1, N):
                    if y[i] == y[k]:
                        for l in range(k+1, N):
                            if y[j] == y[l]:
                                ans += 1
            elif y[i] == y[j]:
                for k in range(j+1, N):
                    if x[i] == x[k]:
                        for l in range(k+1, N):
                            if x[j] == x[l]:
                                ans += 1
    print(ans)
main()
