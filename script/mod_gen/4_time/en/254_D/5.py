def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    x = n >> 1
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) >> 1
        if x in seen: return False
        seen.add(x)
    return True
N = int(input())
count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if is_square(i*j):
            count += 1
print(count)

if __name__ == '__main__':
    is_square()