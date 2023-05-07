def main():
    N = int(input())
    d = {}
    for i in range(N):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_v = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_v:
            print(k)
