def common_divisor(a,b):
    # A,Bの最大公約数を求める
    while b:
        a,b = b,a%b
    return a
a,b,k = map(int,input().split())
c = common_divisor(a,b)
l = []
for i in range(1,c+1):
    if c % i == 0:
        l.append(i)
print(l[-k])
