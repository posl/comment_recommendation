def main():
    # 1. Input
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    # 2. Process
    if n == 0:
        ans = x
    else:
        p.sort()
        if x < p[0]:
            ans = p[0] - 1
        elif p[-1] < x:
            ans = p[-1] + 1
        else:
            for i in range(n - 1):
                if p[i] <= x and x <= p[i + 1]:
                    if x - p[i] < p[i + 1] - x:
                        ans = p[i]
                    elif x - p[i] > p[i + 1] - x:
                        ans = p[i + 1]
                    else:
                        ans = p[i]
                    break
    # 3. Output
    print(ans)
