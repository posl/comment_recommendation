def f(m, a):
    return sum([m % i for i in a])
n = int(input())
a = list(map(int, input().split()))
ok = 0
ng = 10**9 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid, a) < f(mid + 1, a):
        ng = mid
    else:
        ok = mid
print(f(ok + 1, a))

if __name__ == '__main__':
    f()