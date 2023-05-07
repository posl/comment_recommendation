def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    if x < p[0]:
        print(p[0])
        return
    if x > p[-1]:
        print(p[-1])
        return
    for i in range(n):
        if p[i] == x:
            print(p[i+1])
            return
        if p[i+1] > x:
            if p[i+1] - x < x - p[i]:
                print(p[i+1])
                return
            else:
                print(p[i])
                return
