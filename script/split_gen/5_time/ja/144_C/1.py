def main():
    n = int(input())
    ans = 0
    for i in range(2, n+1):
        if i*i <= n:
            ans += n//i - 1
        else:
            ans += n//i
    print(ans)
