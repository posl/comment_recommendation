def main():
    v,a,b,c = map(int, input().split())
    if a <= b and a <= c:
        print("F")
    elif b <= a and b <= c:
        print("M")
    elif c <= a and c <= b:
        print("T")
