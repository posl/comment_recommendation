def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        a[i] = a[i] % a[0]
    if a[0] == 1:
        print(1)
    else:
        print(a[0])
