def sum_of_natural_nums(n):
    return n*(n+1)/2
n = int(raw_input())
sum = 0
for i in range(n):
    a, b = map(int, raw_input().split())
    sum += sum_of_natural_nums(b) - sum_of_natural_nums(a-1)
print sum

if __name__ == '__main__':
    sum_of_natural_nums()