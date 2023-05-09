def main():
    n = int(input())
    p = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if p[i] == i:
            c += 1
    if c == n:
        print(n)
    else:
        print(n-1)
