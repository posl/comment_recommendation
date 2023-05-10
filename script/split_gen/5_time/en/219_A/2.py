def main():
    points = int(input())
    if points < 40:
        print(40 - points)
    elif points < 70:
        print(70 - points)
    elif points < 90:
        print(90 - points)
    else:
        print("expert")
