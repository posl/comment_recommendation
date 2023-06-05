def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.reverse()
    h = 0
    for i in range(n):
        if a[i] > h:
            h = a[i]
        elif a[i] < h:
            a[i] = h
    a.reverse()
    print(sum(a))
