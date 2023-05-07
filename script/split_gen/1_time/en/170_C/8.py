def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    p.append(101)
    p.insert(0, -1)
    ans = 0
    for i in range(1, N + 2):
        if p[i] - p[i - 1] == 2:
            ans = p[i] - 1
            break
        elif p[i] - p[i - 1] == 1:
            continue
        else:
            if abs(p[i] - X) < abs(p[i - 1] - X):
                ans = p[i]
            else:
                ans = p[i - 1]
            break
    print(ans)
