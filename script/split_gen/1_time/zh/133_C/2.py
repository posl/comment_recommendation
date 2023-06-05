def main():
    l,r = map(int,input().split())
    if l == r:
        print(l%2019)
        return
    elif r - l >= 2019:
        print(0)
        return
    else:
        ans = 2018
        for i in range(l,r):
            for j in range(i+1,r+1):
                ans = min(ans,(i*j)%2019)
        print(ans)
        return
