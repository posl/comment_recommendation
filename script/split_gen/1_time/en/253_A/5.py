def main():
    #a, b, c = map(int, input().split())
    a, b, c = map(int, "2 5 3".split())
    if b <= a and b >= c or b >= a and b <= c:
        print("Yes")
    else:
        print("No")
