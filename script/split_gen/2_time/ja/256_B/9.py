def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p += 1
            continue
        p += 1
        if i + a[i] >= 4:
            p -= 1
    print(p)
