def check(n):
    return all([str(n).count(c) > 0 for c in '753'])
N = int(input())
print(sum([check(n) for n in range(357, N+1, 2)]))
