def main():
    p = int(input())
    ans = 0
    for i in range(10,0,-1):
        ans += p // math.factorial(i)
        p %= math.factorial(i)
    print(ans)
