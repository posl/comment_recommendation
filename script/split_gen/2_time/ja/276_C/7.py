def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    #print(p)
    a = [i for i in range(n)]
    #print(a)
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                a[i], a[j] = a[j], a[i]
    for i in range(n):
        print(a[i] + 1, end=' ')
    print()
