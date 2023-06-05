def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    cnt = 0
    i = 0
    j = 0
    while i < n and j < n:
        if a[i] > b[j]:
            cnt += 1
            i += 1
        j += 1
    print(cnt)
