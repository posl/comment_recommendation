def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_tmp, b_tmp = map(int, input().split())
        a.append(a_tmp)
        b.append(b_tmp)
    c = [0]*(max(a)+max(b)+1)
    for i in range(n):
        for j in range(a[i], a[i]+b[i]):
            c[j] += 1
    for i in range(1, n+1):
        print(c.count(i), end=' ')
