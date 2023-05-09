def main():
    v, a, b, c = map(int, input().split())
    if a*b*c <= v:
        print("M")
    elif a*b <= v or b*c <= v or c*a <= v:
        print("F")
    else:
        print("T")
