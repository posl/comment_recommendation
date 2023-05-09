def main():
    a, b, c = map(int, input().split())
    if b < a:
        a, b = b, a
    if c < b:
        b, c = c, b
    if b == a:
        print("No")
    elif b == c:
        print("No")
    else:
        print("Yes")
