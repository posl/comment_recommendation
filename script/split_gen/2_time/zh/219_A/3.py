def main():
    score = int(input())
    if score >= 90:
        print("expert")
    elif score >= 70:
        print(90 - score)
    elif score >= 40:
