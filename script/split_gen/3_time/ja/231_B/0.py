def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(max(d, key=d.get))
