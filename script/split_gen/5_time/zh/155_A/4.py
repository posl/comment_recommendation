def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("是")
    elif a == c and b != c:
        print("是")
    elif b == c and a != c:
        print("是")
    else:
        print("否")
