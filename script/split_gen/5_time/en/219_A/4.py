def main():
    score = int(input())
    if 0 <= score < 40:
        print(40 - score)
    elif 40 <= score < 70:
        print(70 - score)
    elif 70 <= score < 90:
        print(90 - score)
    else:
        print('expert')
