def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x_min = x[0]
    y_min = y[0]
    x_max = x[-1]
    y_max = y[-1]
    x_min -= 1
    y_min -= 1
    x_max += 1
    y_max += 1
    x = [x_min] + x + [x_max]
    y = [y_min] + y + [y_max]
    #print(x)
    #print(y)
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if i == j == 0:
                continue
            if x[i] == x[i-1] or y[j] == y[j-1]:
                continue
            ans += 1
    print(ans)
