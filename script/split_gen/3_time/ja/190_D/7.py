def calc(n):
    ans = 0
    for i in range(1,n+1):
        if i*(i+1)//2 > n:
            break
        if (n-i*(i+1)//2) % i == 0:
            ans += 1
    return ans*2
n = int(input())
print(calc(n))
