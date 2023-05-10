def main():
    a,b,c,d = map(int, input().split())
    if a > b * c:
        print(-1)
        return
    if a <= b * c:
        if a % (b * d) == 0:
            print(a // (b * d))
            return
        else:
            print(a // (b * d) + 1)
            return
