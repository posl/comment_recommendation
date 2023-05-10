def main():
    l, r = map(int, input().split())
    if (r - l) >= 2019:
        print(0)
        return
    else:
        min_mod = 2018
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                min_mod = min(min_mod, (i * j) % 2019)
        print(min_mod)
        return
