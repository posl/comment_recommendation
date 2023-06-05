def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
a,b,c,d = map(int,input().split())
#求最小公倍数
lcm = c*d//gcd(c,d)
#求出最小公倍数在[a,b]区间内的个数
ans = b//lcm - (a-1)//lcm
print(ans)

if __name__ == '__main__':
    gcd()