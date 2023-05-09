def calc_sum(a, m):
    max_sum = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i + j >= len(a):
                break
            else:
                sum = 0
                for k in range(i, i + j + 1):
                    sum += a[k]
                if sum > max_sum and j + 1 == m:
                    max_sum = sum
    return max_sum
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(calc_sum(a, m))

if __name__ == '__main__':
    calc_sum()