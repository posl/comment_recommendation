def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    ans = 0
    for i in range(n):
        if i == 0 or l[i] > r[i-1]:
            ans += 1
    
    print(ans)
