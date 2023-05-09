def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if t % total == 0:
        print(n, total)
        return
    t %= total
    for i, ai in enumerate(a):
        if t > ai:
            t -= ai
        else:
            print(i+1, t)
            return
