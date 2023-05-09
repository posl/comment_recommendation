def main():
    # X = 56
    # X = 32
    # X = 0
    X = 100
    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    elif X >= 90 and X <= 100:
        print('expert')
    else:
        print('Error')
