def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        if abs(a - (t - h[i] * 0.006)) < min:
            min = abs(a - (t - h[i] * 0.006))
            index = i + 1
    print(index)
