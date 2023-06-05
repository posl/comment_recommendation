def main():
    v,a,b,c = map(int,input().split())
    while v > 0:
        a -= 1
        v -= 1
        if a == 0:
            print("F")
            return
        b -= 1
        v -= 1
        if b == 0:
            print("M")
            return
        c -= 1
        v -= 1
        if c == 0:
            print("T")
            return
