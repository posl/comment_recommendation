def sum_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += sum_natural_numbers(b) - sum_natural_numbers(a - 1)
print(ans)

if __name__ == '__main__':
    sum_natural_numbers()