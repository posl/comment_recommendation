def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if x[i] == x[j]:
                    if x[i] == x[k]:
                        print('Yes')
                        return
                elif y[i] == y[j]:
                    if y[i] == y[k]:
                        print('Yes')
                        return
                elif x[i] != x[j]:
                    if (y[i] - y[j])/(x[i] - x[j]) == (y[i] - y[k])/(x[i] - x[k]):
                        print('Yes')
                        return
    print('No')
    return
