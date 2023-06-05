def get_generation(n, p):
    if n == 1:
        return 0
    else:
        return get_generation(p[n-1], p) + 1
n = int(input())
p = list(map(int, input().split()))
print(get_generation(n, p))
