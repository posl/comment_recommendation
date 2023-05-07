def sport_event(Y):
    while True:
        if Y % 4 == 2:
            return Y
        else:
            Y += 1

if __name__ == '__main__':
    sport_event()