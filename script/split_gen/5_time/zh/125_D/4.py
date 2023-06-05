def main():
    n = int(input())
    a = list(map(int, input().split()))
    minus = 0
    for i in range(n):
        if a[i] < 0:
            minus += 1
    if minus % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - min(map(abs, a)) * 2)
