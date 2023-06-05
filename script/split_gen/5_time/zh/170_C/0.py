def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p_set = set(p)
    ans = 0
    for i in range(102):
        if i not in p_set:
            if abs(x - i) < abs(x - ans):
                ans = i
    print(ans)
