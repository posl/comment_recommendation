def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("是")
    elif b == c and c != a:
        print("是")
    elif c == a and a != b:
        print("是")
    else:
        print("否")
