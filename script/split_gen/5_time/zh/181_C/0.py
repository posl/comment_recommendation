def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (y[i]-y[j])*(x[i]-x[k]) == (x[i]-x[j])*(y[i]-y[k]):
                    print("Yes")
                    exit()
    print("No")
