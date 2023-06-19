def main():
    v,a,b,c = map(int,input().split())
    while v:
        if v < a:
            print("F")
            break
        v -= a
        if v < b:
            print("M")
            break
        v -= b
        if v < c:
            print("T")
            break
        v -= c
