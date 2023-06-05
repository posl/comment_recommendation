def main():
    L, R = map(int, input().split())
    min = 2019
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            if min > (i * j) % 2019:
                min = (i * j) % 2019
    print(min)
