def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    a, b = 0, 0
    for i in range(n):
        if a < b:
            a += t[i]
        else:
            b += t[i]
    print(max(a, b))
