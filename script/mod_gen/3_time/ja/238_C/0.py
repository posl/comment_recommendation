def f(x):
    return len(str(x))
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += f(i)
print(ans % 998244353)

if __name__ == '__main__':
    f()