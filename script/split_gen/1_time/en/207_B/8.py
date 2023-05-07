def main():
    a,b,c,d = map(int, input().split())
    if a > b * d:
        print(-1)
        return
    if c <= d * b:
        print(1)
        return
    print((a + (b * d) - 1) // (b * d))
    return
