def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    else:
        d = []
        for i in range(m-1):
            d.append(x[i+1] - x[i])
        d.sort()
        print(sum(d[:m-n]))
