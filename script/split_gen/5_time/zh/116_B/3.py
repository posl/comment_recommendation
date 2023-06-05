def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s = int(raw_input())
a = [s]
while True:
    s = f(s)
    if s in a:
        break
    a.append(s)
print len(a)+1
