def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("=")
    elif c % 2 == 0:
        if abs(a) == abs(b):
            print("=")
        elif abs(a) > abs(b):
            print(">")
        else:
            print("<")
    elif c % 2 == 1:
        if a > b:
            print(">")
        else:
            print("<")
