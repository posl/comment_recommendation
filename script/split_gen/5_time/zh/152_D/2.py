def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i // 10 == 0:
            ans += 1
        else:
            s = str(i)
            a = int(s[0])
            b = int(s[-1])
            if a == b:
                ans += 1
    print(ans)
