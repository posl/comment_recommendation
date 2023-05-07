def divisor(n): # 約数を求める関数
    d = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    return d
N = int(input())
ans = 0
for i in divisor(math.factorial(N)):
    if len(divisor(i)) == 75:
        ans += 1
print(ans)

if __name__ == '__main__':
    divisor()