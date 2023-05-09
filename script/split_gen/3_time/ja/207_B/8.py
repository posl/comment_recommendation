def main():
    A,B,C,D = map(int,input().split())
    if A <= B*C:
        print(-1)
        return
    ans = 0
    while A > B*C*D:
        A += B
        ans += 1
    print(ans)
