def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("=")
    elif c % 2 == 0:
        a = abs(a)
        b = abs(b)
        if a > b:
            print(">")
        elif a < b:
            print("<")
        else:
            print("=")
    else:
        if a > b:
            print(">")
        else:
            print("<")
