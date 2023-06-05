def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 10 == 0:
            continue
        s = str(i)
        a = s[-1]
        b = s[0]
        if a == b:
            ans += 1
    print(ans)
