def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p += 1
        for j in range(4):
            if j + a[i] >= 4:
                p += 1
    print(p)
