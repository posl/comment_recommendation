def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += 1
        if i >= 10:
            ans += 1
        if i >= 100:
            ans += 1
        if i >= 1000:
            ans += 1
        if i >= 10000:
            ans += 1
        if i >= 100000:
            ans += 1
        if i >= 1000000:
            ans += 1
        if i >= 10000000:
            ans += 1
        if i >= 100000000:
            ans += 1
        if i >= 1000000000:
            ans += 1
        if i >= 10000000000:
            ans += 1
        if i >= 100000000000:
            ans += 1
        if i >= 1000000000000:
            ans += 1
        if i >= 10000000000000:
            ans += 1
        if i >= 100000000000000:
            ans += 1
        if i >= 1000000000000000:
            ans += 1
        if i >= 10000000000000000:
            ans += 1
        if i >= 100000000000000000:
            ans += 1
        if i >= 1000000000000000000:
            ans += 1
    print(ans)
