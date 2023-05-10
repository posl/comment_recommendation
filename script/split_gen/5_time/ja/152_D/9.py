def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        s = str(i)
        a = s[0]
        b = s[-1]
        if a == b:
            ans += 1
    print(ans)
