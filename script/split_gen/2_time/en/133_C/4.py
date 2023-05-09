def main():
    L, R = map(int, input().split())
    if R - L >= 2019:
        print(0)
    else:
        min_mod = 2020
        for i in range(L, R):
            for j in range(i+1, R+1):
                min_mod = min(min_mod, (i*j) % 2019)
        print(min_mod)
