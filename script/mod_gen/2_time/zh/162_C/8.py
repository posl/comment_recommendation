def f(n):
    if n%15 == 0:
        return 0
    elif n%5 == 0:
        return 1
    elif n%3 == 0:
        return 2
    else:
        return 3
N = int(input())
ans = 0
for i in range(1,N+1):
    ans += f(i)*i
print(ans)

if __name__ == '__main__':
    f()