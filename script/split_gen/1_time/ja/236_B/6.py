def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in range(n * 4):
        d[a[i]] = d.get(a[i], 0) + 1
    for k, v in d.items():
        if v % 2 == 1:
            print(k)
            break
