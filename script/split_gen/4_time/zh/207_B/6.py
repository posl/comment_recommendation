def main():
    a,b,c,d = map(int, input().split())
    if a >= b*c:
        print(-1)
    else:
        ans = 0
        while a*d > b:
            a = a*d
            ans += 1
        print(ans)
