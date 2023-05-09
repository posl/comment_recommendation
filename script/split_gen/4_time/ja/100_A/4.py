def main():
    a,b = map(int, input().split())
    if a < 1 or b < 1 or a > 16 or b > 16 or a+b > 16:
        print(":(")
    else:
        print("Yay!")
