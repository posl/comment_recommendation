def main():
    a,b,c,d = [int(x) for x in input().split()]
    if a > b * c:
        print(-1)
    else:
        print((a + b - 1) // b)
