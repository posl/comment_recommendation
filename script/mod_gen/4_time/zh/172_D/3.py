def f(x):
    ans = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            ans += i
            if i != x // i:
                ans += x // i
        i += 1
    return ans
n = int(input())
ans = 0
for k in range(1, n+1):
    ans += k * f(k)
print(ans)

if __name__ == '__main__':
    f()