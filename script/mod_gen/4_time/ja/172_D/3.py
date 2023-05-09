def f(x):
    count = 0
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            count += 1
            if i != x//i:
                count += 1
    return count
n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i*f(i)
print(ans)

if __name__ == '__main__':
    f()