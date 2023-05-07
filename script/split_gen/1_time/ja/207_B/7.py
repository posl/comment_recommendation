def main():
    a,b,c,d = map(int,input().split())
    if a <= b * d:
        print(-1)
        return
    else:
        if a % (b * d - c) == 0:
            print(int(a / (b * d - c)))
        else:
            print(int(a / (b * d - c) + 1))
