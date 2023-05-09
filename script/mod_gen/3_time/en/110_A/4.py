def allowance(a,b,c):
    return max(a+b+c,a*b*c,(a+b)*c,a*(b+c))
a,b,c = map(int,input().split())
print(allowance(a,b,c))
Python 3.6.2

if __name__ == '__main__':
    allowance()