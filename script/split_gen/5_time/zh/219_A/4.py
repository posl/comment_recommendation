def main():
    score = int(input())
    if score < 40:
        print(40 - score)
    elif score < 70:
        print(70 - score)
    elif score < 90:
        print(90 - score)
    else:
        print("专家")
