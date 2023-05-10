def f(x):
    if x == 1:
        return 1
    else:
        count = 2
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if i == x / i:
                    count += 1
                else:
                    count += 2
        return count
n = int(input())
ans = 0
for i in range(n):
    ans += (i + 1) * f(i + 1)
print(ans)

if __name__ == '__main__':
    f()