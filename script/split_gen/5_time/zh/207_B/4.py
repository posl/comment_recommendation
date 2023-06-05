def main():
    a, b, c, d = map(int, input().split())
    if a < b * d:
        print(-1)
    else:
        if (a - b * d) % (b + c) == 0:
            print((a - b * d) // (b + c))
        else:
            print((a - b * d) // (b + c) + 1)
