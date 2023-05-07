def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(n):
        for j in range(i+1, n+1):
            if abs(a[i]-a[j]) == abs(i-j):
                print('No')
                return
    print('Yes')
