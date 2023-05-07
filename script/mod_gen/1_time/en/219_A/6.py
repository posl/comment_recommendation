def main():
    # read input
    score = int(input())
    # process
    if score >= 90:
        answer = 'expert'
    elif score >= 70:
        answer = 90 - score
    elif score >= 40:
        answer = 70 - score
    else:
        answer = 40 - score
    # output
    print(answer)

if __name__ == '__main__':
    main()