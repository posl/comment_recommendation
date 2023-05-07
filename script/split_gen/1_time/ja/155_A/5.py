def main():
    a, b, c = map(int, input().split())
    if a == b:
        if a == c:
            print("No")
        else:
            print("Yes")
    elif a == c:
        print("Yes")
    elif b == c:
        print("Yes")
    else:
        print("No")
