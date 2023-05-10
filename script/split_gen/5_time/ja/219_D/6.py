def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = -1
    for i in range(n):
        if a[i] >= x and b[i] >= y:
            ans = 1
            break
    print(ans)
