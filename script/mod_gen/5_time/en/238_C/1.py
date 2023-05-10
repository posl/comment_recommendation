def f(x):
    if x < 10:
        return x
    else:
        return x % (10 ** len(str(x)))
N = int(input())
sum = 0
for i in range(1, N + 1):
    sum += f(i)
print(sum % 998244353)

if __name__ == '__main__':
    f()