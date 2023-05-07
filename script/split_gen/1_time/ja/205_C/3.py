def main():
    a, b, c = map(int, input().split())
    if a ** c == b ** c:
        print("=")
    elif a ** c > b ** c:
        print(">")
    else:
        print("<")
