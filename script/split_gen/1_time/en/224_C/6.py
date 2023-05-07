def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (x[i]-x[k])*(y[j]-y[k]) != (x[j]-x[k])*(y[i]-y[k]):
                    count += 1
    print(count)
