def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
n,a,b = map(int,input().split())
div = make_divisors(n)
div.sort()
#print(div)
ans = 0
for i in range(len(div)):
    if div[i] == a or div[i] == b:
        continue
    else:
        ans += 1
print(ans)

if __name__ == '__main__':
    make_divisors()