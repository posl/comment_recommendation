def main():
    n, m = map(int, input().split())
    shop = []
    for i in range(n):
        shop.append(list(map(int, input().split())))
    shop.sort(key=lambda x: x[0])
    count = 0
    for i in range(n):
        if shop[i][1] >= m:
            count += shop[i][0] * m
            return count
        else:
            count += shop[i][0] * shop[i][1]
            m -= shop[i][1]
