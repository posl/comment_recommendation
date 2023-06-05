def f(m, a):
    sum = 0
    for i in a:
        sum += m % i
    return sum
n = int(input())
a = list(map(int, input().split()))
print(f(max(a), a))
