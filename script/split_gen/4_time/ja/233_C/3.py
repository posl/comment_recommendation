def main():
    n,x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1,2**n):
        s = 1
        for j in range(n):
            if i & (1<<j):
                s *= l[j][0]
        if s == x:
            ans += 1
    print(ans)
