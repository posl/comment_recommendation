def solve(n, a):
    count = 0
    while True:
        if all([i%2==0 for i in a]):
            a = [i/2 for i in a]
            count += 1
        elif all([i%3==0 for i in a]):
            a = [i/3 for i in a]
            count += 1
        elif all([i==a[0] for i in a]):
            return count
        else:
            return -1
n = int(raw_input())
a = map(int, raw_input().split())
print solve(n, a)
