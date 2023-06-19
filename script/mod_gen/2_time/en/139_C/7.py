def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    m = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            c += 1
        else:
            c = 0
        m = max(m, c)
    print(m)
main()
