def main():
    a, b, c = map(int, input().split())
    if a == b and b != c or a == c and b != c or b == c and a != c:
        print("是")
    else:
        print("否")
