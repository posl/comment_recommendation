def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p += 1
        p += (p + a[i]) // 4
        p -= (p + a[i]) // 4 * 4
    print(p)
