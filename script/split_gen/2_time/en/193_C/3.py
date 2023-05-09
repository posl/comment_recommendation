def main():
    N = int(input())
    from math import log
    ans = 0
    for a in range(2, int(log(N, 2)) + 2):
        for b in range(2, int(log(N, a)) + 2):
            if N >= a ** b:
                ans += 1
            else:
                break
    print(N - ans)
