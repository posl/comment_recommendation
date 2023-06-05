def count_divide_2(num):
    count = 0
    while num % 2 == 0:
        num = num // 2
        count += 1
    return count
n = int(input())
a = list(map(int, input().split()))
count = 0
for num in a:
    count += count_divide_2(num)
print(count)

if __name__ == '__main__':
    count_divide_2()