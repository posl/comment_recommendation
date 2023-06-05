def getFee(age):
    if age <= 5:
        return 0
    elif age <= 12:
        return 50
    else:
        return 100

if __name__ == '__main__':
    getFee()