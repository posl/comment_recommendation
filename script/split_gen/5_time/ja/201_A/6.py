def main():
    a,b,c = map(int, input().split())
    if a - b == b - c or a - c == c - b or b - a == a - c or b - c == c - a or c - a == a - b or c - b == b - a:
        print("Yes")
    else:
        print("No")
