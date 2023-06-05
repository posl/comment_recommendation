def main():
    n = int(input())
    p = []
    for i in range(0,n):
        p.append(int(input()))
    p.sort()
    p[n-1] = int(p[n-1]/2)
    print(sum(p))
