def main():
    v,a,b,c = map(int,input().split())
    while True:
        if v < a:
            print("F")
            break
        else:
            v -= a
        if v < b:
            print("M")
            break
        else:
            v -= b
        if v < c:
            print("T")
            break
        else:
            v -= c
