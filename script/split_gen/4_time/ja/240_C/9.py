def main():
    n,x = map(int, input().split())
    d = 0
    for i in range(n):
        a,b = map(int, input().split())
        d += b - a
    if abs(d) <= x:
        print('Yes')
    else:
        print('No')
