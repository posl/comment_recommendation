def main():
    n = int(input())
    a = list(map(int, input().split()))
    h = 0
    for i in range(n-1, -1, -1):
        if a[i] > h:
            h = a[i]
        elif a[i] < h:
            h = a[i] = h
    print(sum(a))
