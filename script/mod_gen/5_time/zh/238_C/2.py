def f(x):
    return int(x*(10**(len(str(x)))-1)/9)
N = int(input())
ans = 0
for i in range(1,10):
    if f(i) <= N:
        ans += i
    else:
        ans += N - 10**(len(str(i))-1) + 1
        break
print(ans%998244353)

if __name__ == '__main__':
    f()