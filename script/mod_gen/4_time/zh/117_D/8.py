def f(x, a):
    result = 0
    for i in range(len(a)):
        result += x ^ a[i]
    return result
n, k = map(int, input().split())
a = list(map(int, input().split()))

if __name__ == '__main__':
    f()