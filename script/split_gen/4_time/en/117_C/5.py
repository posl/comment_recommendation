def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    dist = []
    for i in range(m-1):
        dist.append(x[i+1]-x[i])
    dist.sort()
    print(sum(dist[:m-n]))
