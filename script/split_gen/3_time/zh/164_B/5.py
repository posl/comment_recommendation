def main():
    a,b,c,d = map(int, input().split())
    while 1:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
