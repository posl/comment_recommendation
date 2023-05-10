def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    diff = 100
    ans = 100
    for i in range(102):
        if i not in p and diff > abs(x - i):
            diff = abs(x - i)
            ans = i
    print(ans)
