def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            b.sort()
            m.append(b[(j-i)//2])
    m.sort()
    print(m[len(m)//2])
