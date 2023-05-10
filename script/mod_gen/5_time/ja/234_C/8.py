def f(k):
    if k == 0:
        return 0
    if k == 1:
        return 2
    if k % 2 == 0:
        return f(k//2) * 10 + 2
    else:
        return f(k//2) * 10
k = int(input())
print(f(k))

if __name__ == '__main__':
    f()