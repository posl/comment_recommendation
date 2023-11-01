def get_level(score):
    if 0 <= score < 40:
        return "D"
    elif 40 <= score < 70:
        return "C"
    elif 70 <= score < 90:
        return

if __name__ == '__main__':
    get_level()