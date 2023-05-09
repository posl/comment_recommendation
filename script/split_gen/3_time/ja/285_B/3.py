def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for k in range(1, n - i):
            if s[k - 1] != s[k + i - 1]:
                l = k
        print(l)
