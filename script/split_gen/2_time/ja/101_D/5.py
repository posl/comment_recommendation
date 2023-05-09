def f(n):
    return n / sum(map(int, str(n)))
K = int(input())
n = 1
s = [1]
while len(s) < K:
    n += 1
    if f(n) >= f(s[-1]):
        s.append(n)
for i in s:
    print(i)
