def f(m, a):
    return sum([m % i for i in a])
n = int(input())
a = list(map(int, input().split()))
a.sort()
max_a = a[-1]
min_a = a[0]
max_f = 0
for i in range(min_a, max_a + 1):
    max_f = max(max_f, f(i, a))
print(max_f)

if __name__ == '__main__':
    f()