def main():
    a,b,c,d,e = map(int, input().split())
    if (a == b and c == d and c == e) or (a == b and a == c and d == e):
        print("Yes")
    else:
        print("No")
