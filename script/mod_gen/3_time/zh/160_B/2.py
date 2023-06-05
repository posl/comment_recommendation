def max_happy(x):
    happy = 0
    while x >= 500:
        x -= 500
        happy += 1000
    while x >= 5:
        x -= 5
        happy += 5
    return happy

if __name__ == '__main__':
    max_happy()