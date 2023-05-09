def main():
    A, B = map(int, input().split())
    if A >= 15 or B >= 15 or A + B >= 16:
        print(":(")
    else:
        print("Yay!")
