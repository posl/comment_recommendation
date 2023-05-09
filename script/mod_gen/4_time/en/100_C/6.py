def count_divide_2(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2
    return count
N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(N):
    count += count_divide_2(A[i])
print(count)

if __name__ == '__main__':
    count_divide_2()