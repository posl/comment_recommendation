def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    dx = []
    for i in range(m-1):
        dx.append(x[i+1]-x[i])
    dx.sort()
    print(sum(dx[:m-n]))
