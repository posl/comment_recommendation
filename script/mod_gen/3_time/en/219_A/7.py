def main():
    # get the score
    score = int(input())
    # if the score is less than 40 print 40 - score
    if score < 40:
        print(40 - score)
    # if the score is less than 70 print 70 - score
    elif score < 70:
        print(70 - score)
    # if the score is less than 90 print 90 - score
    elif score < 90:
        print(90 - score)
    # if the score is less than 100 print expert
    elif score < 100:
        print("expert")
    # if the score is 100 print expert
    elif score == 100:
        print("expert")

if __name__ == '__main__':
    main()