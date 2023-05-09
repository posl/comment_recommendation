def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N, 0, -1):
        s = 0
        for j in range(i, N+1, i):
            s += a[j-1]
        if s%2 != a[i-1]:
            b.append(i)
    print(len(b))
    print(*b)
