def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1
s = int(input())
l = [s]
while True:
    s = f(s)
    if s in l:
        print(l.index(s)+1)
        break
    else:
        l.append(s)
