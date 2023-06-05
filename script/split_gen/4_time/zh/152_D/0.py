def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        a = str(i)
        b = a[::-1]
        if a[0] == b[-1] and a[-1] == b[0]:
            ans += 1
    print(ans)
