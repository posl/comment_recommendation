def divisors(n):
    divs = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return divs
N = int(input())
ans = 0
for i in range(1,N+1,2):
    if len(divisors(i)) == 8:
        ans += 1
print(ans)

if __name__ == '__main__':
    divisors()