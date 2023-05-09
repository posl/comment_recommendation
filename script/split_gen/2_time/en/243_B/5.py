def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    c = 0
    d = 0
    while i < n and j < n:
        if a[i] == b[j]:
            c += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    i = 0
    j = 0
    while i < n and j < n:
        if a[i] == b[j]:
            if i != j:
                d += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(c)
    print(d)
