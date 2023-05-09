def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40-x)
    elif x >= 40 and x < 70:
        print(70-x)
    elif x >= 70 and x < 90:
        print(90-x)
    elif x >= 90 and x <= 100:
        print("expert")
    else:
        print("error")
