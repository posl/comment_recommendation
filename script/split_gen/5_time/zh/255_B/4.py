def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        p,q = map(int, input().split())
        x.append(p)
        y.append(q)
    print(x)
    print(y)
    print(a)
