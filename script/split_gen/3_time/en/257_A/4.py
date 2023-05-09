def main():
    N, X = map(int, input().split())
    a = 0
    for i in range(1, N+1):
        if X <= i*26:
            a = i
            break
    b = X - (a-1)*26
    c = chr(b+64)
    print(c)
