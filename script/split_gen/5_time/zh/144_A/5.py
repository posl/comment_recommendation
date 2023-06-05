def main():
    a,b = map(int,input().split())
    if (a > 0 and a < 21) and (b > 0 and b < 21):
        print(a*b)
    else:
        print(-1)
