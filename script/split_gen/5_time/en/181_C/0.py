def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j]):
                    print("Yes")
                    exit()
    print("No")
