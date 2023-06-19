def f(A, B):
    return A ^ B ^ ((A ^ B) + 1) >> 1
A, B = map(int, input().split())
print(f(A, B))
