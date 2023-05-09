def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        li, ri = map(int, input().split())
        if li > l:
            l = li
        if ri < r:
            r = ri
    if l <= r:
        print(r - l + 1)
    else:
        print(0)
