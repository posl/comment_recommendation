def main():
    a,b,c = map(int, input().split())
    if (a == b and b != c) or (b == c and a != c) or (a == c and a != b):
        print("Yes")
    else:
        print("No")
