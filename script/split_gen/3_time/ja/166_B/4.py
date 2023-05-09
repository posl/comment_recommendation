def main():
    n, k = map(int, input().split())
    d = [0] * n
    for i in range(k):
        di = int(input())
        for j in map(int, input().split()):
            d[j - 1] += 1
    print(d.count(0))
