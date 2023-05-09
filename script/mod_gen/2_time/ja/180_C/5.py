def divisors(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
        i += 1
    return res
n = int(input())
ans = divisors(n)
ans.sort()
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    divisors()