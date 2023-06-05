def main():
    n = int(input())
    a = []
    for i in range(n):
        if i == 0:
            a.append([1])
        elif i == 1:
            a.append([1,1])
        else:
            a.append([1])
            for j in range(1,i):
                a[i].append(a[i-1][j-1]+a[i-1][j])
            a[i].append(1)
    for i in range(n):
        print(' '.join([str(j) for j in a[i]]))
