def christmas_eve():
    day = int(input())
    if day == 25:
        print("Christmas")
    elif day == 24:
        print("Christmas Eve")
    elif day == 23:
        print("Christmas Eve Eve")
    elif day == 22:
        print("Christmas Eve Eve Eve")

if __name__ == '__main__':
    christmas_eve()