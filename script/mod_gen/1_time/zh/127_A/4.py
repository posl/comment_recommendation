def get_fee(age):
    if age >= 13:
        return 100
    elif age >= 6:
        return 50
    else:
        return 0

if __name__ == '__main__':
    get_fee()