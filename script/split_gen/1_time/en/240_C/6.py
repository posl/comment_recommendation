def main():
    n, x = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 'No'
    for i in range(n):
        if a[i] <= x <= b[i]:
            ans = 'Yes'
    print(ans)
