def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if not "7" in str(i) and not "7" in oct(i):
            ans += 1
    print(ans)
