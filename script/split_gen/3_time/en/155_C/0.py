def main():
    N = int(input())
    d = {}
    for i in range(N):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_count = max(d.values())
    for k in sorted(d.keys()):
        if d[k] == max_count:
            print(k)
