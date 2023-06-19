def main():
    n = int(input())
    t = list(map(int, input().split()))
    if n == 1:
        print(t[0])
        return
    if n == 2:
        print(max(t))
        return
    t.sort(reverse=True)
    a = t[0]
    b = t[1]
    for i in range(2, n):
        if a > b:
            b += t[i]
        else:
            a += t[i]
    print(max(a, b))
