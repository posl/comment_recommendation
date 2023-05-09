def f(A, B):
    if A == B:
        return A
    if A % 2 == 0 and B % 2 == 1:
        return 1
    if A % 2 == 1 and B % 2 == 0:
        return 0
    if A % 2 == 0 and B % 2 == 0:
        return f(A // 2, B // 2)
    if A % 2 == 1 and B % 2 == 1:
        return f(A // 2, B // 2)
A, B = map(int, input().split())
print(f(A, B))

if __name__ == '__main__':
    f()