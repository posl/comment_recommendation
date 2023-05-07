def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int, input().split()))
        l = tuple(l[1:])
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    print(len(d))
