def main():
    x = input()
    x = int(x)
    if 0 <= x < 40:
        print(40 - x)
    elif 40 <= x < 70:
        print(70 - x)
    elif 70 <= x < 90:
        print(90 - x)
    else:
        print("专家")
