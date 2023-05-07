def check(n, k):
    if k % 2 == 0:
        return n // k * n // k * n // k + (n // k + 1) * (n // k + 1) * (n // k + 1)
    else:
        return n // k * n // k * n // k
n, k = map(int, input().split())
print(check(n, k))

if __name__ == '__main__':
    check()