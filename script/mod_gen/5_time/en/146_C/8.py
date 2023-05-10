def d(n):
    return len(str(n))
import sys
A,B,X = map(int,sys.stdin.readline().strip().split())
#print(A,B,X)
#A,B,X = map(int,"1234 56789 314159265".strip().split())
#print(A,B,X)
l = 0
r = 10**9
while l<r:
    m = (l+r+1)//2
    if A*m+B*d(m)<=X:
        l = m
    else:
        r = m-1
print(l)

if __name__ == '__main__':
    d()