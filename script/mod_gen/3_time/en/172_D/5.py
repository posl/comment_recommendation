def f(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return 2*f(x//2)
    else:
        return 2*f((x+1)//2)
N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i*f(i)
print(ans)

if __name__ == '__main__':
    f()