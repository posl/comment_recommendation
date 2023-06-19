def is_square(n):
    return n == int(n**.5)**2
N = int(input())
ans = 0
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if is_square(i * j):
            if i == j:
                ans += 1
            else:
                ans += 2
print(ans)

if __name__ == '__main__':
    is_square()