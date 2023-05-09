def main():
    a, b, c, d, e, f, x = map(int, input().split())
    taka = (a + c) * b
    aoki = d * e
    if taka > aoki:
        print("Takahashi")
    elif aoki > taka:
        print("Aoki")
    else:
        print("Draw")
