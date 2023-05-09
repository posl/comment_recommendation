def pascal(n):
    a = []
    for i in range(n):
        a.append([1]*(i+1))
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a
n = int(input())
a = pascal(n)
for i in a:
    print(' '.join(map(str,i)))

if __name__ == '__main__':
    pascal()