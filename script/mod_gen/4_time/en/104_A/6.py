def next_contest():
    rating = input()
    if int(rating) < 1200:
        print("ABC")
    elif int(rating) >= 1200 and int(rating) < 2800:
        print("ARC")
    else:
        print("AGC")
next_contest()

if __name__ == '__main__':
    next_contest()