def main():
    n,m = map(int, input().split())
    sc = [list(map(int, input().split())) for i in range(m)]
    ans = -1
    for i in range(10**(n-1), 10**n):
        s = str(i)
        for j in range(m):
            if int(s[sc[j][0]-1]) != sc[j][1]:
                break
        else:
            ans = i
            break
    print(ans)
