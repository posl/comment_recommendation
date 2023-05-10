def main():
    n, m = map(int, input().split())
    a = [0] * n
    def rec(i):
        if i == n:
            print(' '.join(map(str, a)))
            return
        for j in range(1, m + 1):
            a[i] = j
            rec(i + 1)
    rec(0)
