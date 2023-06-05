def f(m):
    result = 0
    for i in range(N):
        result += m % a[i]
    return result
N = int(input())
a = list(map(int, input().split()))

if __name__ == '__main__':
    f()