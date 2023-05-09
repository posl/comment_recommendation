def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i:
            count += 1
    if count == n:
        print(n)
    else:
        print(n - 1)
