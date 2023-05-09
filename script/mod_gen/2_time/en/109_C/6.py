def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n,x=map(int,input().split())
xlist=list(map(int,input().split()))
xlist.sort()
xlist=[i-x for i in xlist]
d=abs(xlist[0])
for i in xlist:
    d=gcd(d,abs(i))
print(d)
It's not the fastest solution, but it's a nice one-liner. It's a bit slow on the last sample input, but I think that's because of the gcd function. I'm not sure how to improve it.
I'm a bit confused about the problem statement. Can there be multiple cities at the same coordinate? Or are all the coordinates different?
There are no cities at the same coordinate.
I'm a bit confused about the problem statement. Can there be multiple cities at the same coordinate? Or are all the coordinates different?
The coordinates are different. The statement is a bit confusing though.
I've tried to make it clea

if __name__ == '__main__':
    gcd()