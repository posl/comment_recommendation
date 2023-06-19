def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    ans = 0
    if r-1 >= 1:
        ans += 1
    if r+1 <= h:
        ans += 1
    if c-1 >= 1:
        ans += 1
    if c+1 <= w:
        ans += 1
    print(ans)
main()
