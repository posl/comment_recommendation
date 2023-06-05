def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(m - 1, -1, -1):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        if a[i] == b[i]:
            ans += 1
            continue
        if a[i] == 1:
            for j in range(i + 1, m + 1):
                if a[j] < b[i] and b[j] >= b[i]:
                    ans += 1
        else:
            for j in range(i + 1, m + 1):
                if a[j] < a[i] and b[j] >= a[i]:
                    ans += 1
    print(ans)
