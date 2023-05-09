def calc_sum(a, b):
    return a * b
n = int(input())
d = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i+1, n):
        sum += calc_sum(d[i], d[j])
print(sum)

if __name__ == '__main__':
    calc_sum()