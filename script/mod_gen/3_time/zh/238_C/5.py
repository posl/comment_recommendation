def f(x):
    return x
N = int(input())
ans = 0
for i in range(1, N+1):
    ans += f(i)
    ans %= 998244353
print(ans)

if __name__ == '__main__':
    f()