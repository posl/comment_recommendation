def sum_of_n(n):
    return (n * (n + 1)) // 2
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += sum_of_n(b) - sum_of_n(a - 1)
print(sum)

if __name__ == '__main__':
    sum_of_n()