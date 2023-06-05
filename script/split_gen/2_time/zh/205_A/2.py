def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 < oven2:
            oven1 += t[i]
        else:
            oven2 += t[i]
    print(max(oven1, oven2))
