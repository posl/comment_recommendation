def divisor(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
    return res
N = int(input())
count = 0
for i in range(1, N+1, 2):
    if len(divisor(i)) == 8:
        count += 1
print(count)

if __name__ == '__main__':
    divisor()