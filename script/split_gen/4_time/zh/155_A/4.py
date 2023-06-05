def main():
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("是")
    elif a == c and a != b:
        print("是")
    elif b == c and b != a:
        print("是")
    else:
        print("否")
