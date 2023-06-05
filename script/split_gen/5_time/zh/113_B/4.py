def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    res = abs(a - (t - h[0] * 0.006))
    index = 1
    for i in range(1, n):
        tmp = abs(a - (t - h[i] * 0.006))
        if tmp < res:
            res = tmp
            index = i + 1
    print(index)
