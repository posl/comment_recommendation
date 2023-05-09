def main():
    n = int(input())
    d = {}
    for i in range(n):
        l, *a = map(int, input().split())
        s = ' '.join(map(str, a))
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(len(d))
