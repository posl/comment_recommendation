def S(n):
    return sum(map(int,str(n)))
k = int(input())
a = []
n = 0
while len(a) < k:
    n += 1
    if n % S(n) == 0:
        a.append(n)
print(*a,sep="\n")
