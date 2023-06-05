def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.insert(0, 0)
    b = [0]*(2*n+1)
    for i in range(1, n+1):
        b[a[i]] = i
    for i in range(1, n+1):
        j = b[i]
        ans = 0
        while j > 1:
            j //= 2
            ans += 1
        print(ans)
