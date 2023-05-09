def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    aoki = sum(a)
    takahashi = 0
    for i in range(n):
        takahashi += a[i] + b[i]
    takahashi /= 2
    if aoki < takahashi:
        print(0)
    else:
        a.sort(reverse=True)
        b.sort(reverse=True)
        count = 0
        for i in range(n):
            aoki -= a[i]
            takahashi -= a[i] + b[i]
            count += 1
            if aoki < takahashi:
                break
        print(count)
