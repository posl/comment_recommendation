def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    ans = "No"
    for i in range(n):
        if a[i] <= x and b[i] > 0:
            ans = "Yes"
    print(ans)
