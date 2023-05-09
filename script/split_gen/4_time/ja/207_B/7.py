def main():
    a,b,c,d = map(int,input().split())
    ans = 0
    if (a > b * c):
        ans = -1
    else:
        ans = (a + (b * c) - 1) // (b * c)
    print(ans)
