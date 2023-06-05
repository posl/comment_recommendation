def main():
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
        exit()
    min_num = 2019
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            min_num = min(min_num, (i * j) % 2019)
            if min_num == 0:
                print(0)
                exit()
    print(min_num)
