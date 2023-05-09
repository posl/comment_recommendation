def main():
    L, R = map(int, input().split())
    if R - L >= 2019:
        print(0)
        return
    else:
        min_val = 2018
        for i in range(L, R):
            for j in range(i+1, R+1):
                if min_val > ((i * j) % 2019):
                    min_val = (i * j) % 2019
        print(min_val)
        return
