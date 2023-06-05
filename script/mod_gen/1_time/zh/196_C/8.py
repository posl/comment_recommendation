def count(N):
    if N<11:
        return 0
    if N<100:
        return 1
    if N<1000:
        return 10
    if N<10000:
        return 100
    if N<100000:
        return 1000
    if N<1000000:
        return 10000
    if N<10000000:
        return 100000
    if N<100000000:
        return 1000000
    if N<1000000000:
        return 10000000
    if N<10000000000:
        return 100000000
    if N<100000000000:
        return 1000000000
    if N<1000000000000:
        return 10000000000
    else:
        return 100000000000
N=int(input())
print(count(N))
