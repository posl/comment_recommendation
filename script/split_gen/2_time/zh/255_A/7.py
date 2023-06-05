def main():
    from math import sqrt
    n = int(input())
    res = 0
    for i in range(1, int(sqrt(n))+1):
        for j in range(i, n//i+1):
            if i * j <= n:
                res += 1
    print(res)
