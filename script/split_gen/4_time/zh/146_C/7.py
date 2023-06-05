def main():
    A, B, X = map(int, input().split())
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        c = (l + r) // 2
        if A * c + B * len(str(c)) <= X:
            l = c
        else:
            r = c
    print(l)
