def median(l):
    l.sort()
    return l[(len(l)-1)/2]
    
n = int(raw_input())
a = map(int, raw_input().split())
b = []
for i in range(n):
    for j in range(i, n):
        b.append(median(a[i:j+1]))
print median(b)
