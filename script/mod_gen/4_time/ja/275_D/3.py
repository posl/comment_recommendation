def f(N):
    if N == 0:
        return 1
    return f(N//2) + f(N//3)
N = int(input())
print(f(N))
