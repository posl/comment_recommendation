def f(x):
    sum = 0
    for a in A:
        sum += (x^a)
    return sum
N, K = map(int, input().split())
A = list(map(int, input().split()))
max = 0
for i in range(K+1):
    if f(i) > max:
        max = f(i)
print(max)

if __name__ == '__main__':
    f()