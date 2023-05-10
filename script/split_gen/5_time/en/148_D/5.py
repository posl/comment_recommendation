def main():
    n = int(input())
    a = list(map(int, input().split()))
    broken = 0
    for i in range(n):
        if a[i] == i+1:
            broken += 1
    if broken == n:
        print(-1)
    else:
        print(n - broken)
