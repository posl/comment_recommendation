def max_f(m, a):
    f = 0
    for i in range(len(a)):
        f += m % a[i]
    return f
N = int(input())
a = list(map(int, input().split()))

if __name__ == '__main__':
    max_f()