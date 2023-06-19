def main():
    n,k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    #print(d)
    #print(a)
    ans = 0
    for i in range(n):
        for j in range(k):
            if i+1 not in a[j]:
                ans += 1
    print(ans)
    return
