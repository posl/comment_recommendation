def binary_search(a,x):
    left = 0
    right = len(a)-1
    while left <= right:
        mid = int((left + right)/2)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
a,b,q = map(int,input().split())
s = []
t = []
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x = int(input())
    x1 = binary_search(s,x)
    x2 = binary_search(t,x)
    ans = 10**20
    for ss in s[x1-1:x1+1]:
        for tt in t[x2-1:x2+1]:
            d1 = abs(ss-x) + abs(tt-ss)
            d2 = abs(tt-x) + abs(ss-tt)
            ans = min(ans,d1,d2)
    print(ans)

if __name__ == '__main__':
    binary_search()