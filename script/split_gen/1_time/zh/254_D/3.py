def f(n):
    import math
    ans = 0
    for i in range(1,int(math.sqrt(n))+1):
        ans += int(n/i)-i+1
    return ans
n = int(input())
print(f(n))
