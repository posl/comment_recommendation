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
        for j in range(n):
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x and y[j] in y:
                    ans += 1
    print(ans)
