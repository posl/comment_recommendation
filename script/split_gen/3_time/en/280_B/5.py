def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join([str(x) for x in a]))
