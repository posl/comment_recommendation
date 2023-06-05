def f(m):
    sum = 0
    for i in range(N):
        sum += m % a[i]
    return sum
N = int(input())
a = list(map(int, input().split()))
a.sort()

if __name__ == '__main__':
    f()