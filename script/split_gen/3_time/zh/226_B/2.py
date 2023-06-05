def main():
    n = int(input())
    d = {}
    for i in range(n):
        tmp = tuple(map(int, input().split()))
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 1
    print(len(d))
