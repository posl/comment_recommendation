def main():
    # Get input
    a, b, k = map(int, input().split())
    # If k is greater than the sum of a and b, then both of them will have 0 cookies
    if k >= a + b:
        print(0, 0)
    # If k is greater than a, then a will have 0 cookies, and b will have b - (k - a)
    elif k >= a:
        print(0, b - (k - a))
    # Otherwise, both of them will have a - k and b
    else:
        print(a - k, b)
