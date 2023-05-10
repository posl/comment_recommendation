def main():
    # get input
    a, b = map(int, input().split())
    # your code
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(int(b/2))
    else:
        print(0)
