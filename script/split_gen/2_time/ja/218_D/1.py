def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                if x[i] == x[j] and y[i] == y[k]:
                    for l in range(k+1,n):
                        if x[i] == x[l] and y[j] == y[l]:
                            ans += 1
    print(ans)
