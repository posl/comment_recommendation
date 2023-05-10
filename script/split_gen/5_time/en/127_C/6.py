def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        l_i, r_i = map(int, input().split())
        if l_i > l:
            l = l_i
        if r_i < r:
            r = r_i
    if r >= l:
        print(r - l + 1)
    else:
        print(0)
