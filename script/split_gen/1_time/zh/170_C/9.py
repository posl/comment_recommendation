def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    ans = x
    for i in range(102):
        if i in p:
            continue
        if abs(x - i) < abs(x - ans):
            ans = i
    print(ans)
