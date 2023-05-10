def func(a, b, k):
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    return cnt
a, b, k = map(int, input().strip().split())
print(func(a, b, k))

if __name__ == '__main__':
    func()